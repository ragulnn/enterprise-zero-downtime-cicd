pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20'))
        timeout(time: 30, unit: 'MINUTES')
    }

    environment {
        IMAGE_NAME = "enterprise-backend"
        IMAGE_TAG = "${BUILD_NUMBER}"

        ACR_NAME = "ragulm175acr"
        ACR_LOGIN_SERVER = "ragulm175acr.azurecr.io"

        K8S_NAMESPACE = "enterprise"
        DEPLOYMENT_NAME = "enterprise-backend"
        SERVICE_NAME = "enterprise-backend"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ragulnn/enterprise-zero-downtime-cicd.git'
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                set -e

                echo "=================================="
                echo "VERIFYING BUILD ENVIRONMENT"
                echo "=================================="

                whoami
                pwd

                echo ""
                docker --version

                echo ""
                kubectl version --client

                echo ""
                echo "===== Kubernetes Context ====="

                CURRENT_CONTEXT=$(kubectl config current-context)

                echo "Current Context: $CURRENT_CONTEXT"

                if [ "$CURRENT_CONTEXT" != "enterprise-aks" ]; then
                    echo "ERROR: Jenkins is NOT connected to AKS!"
                    exit 1
                fi

                echo ""
                echo "===== Kubernetes Nodes ====="

                kubectl get nodes

                echo ""
                az --version
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('Local-SonarQube') {

                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                          -Dsonar.projectKey=enterprise-zero-downtime-cicd \
                          -Dsonar.projectName=enterprise-zero-downtime-cicd \
                          -Dsonar.sources=backend \
                          -Dsonar.python.version=3.12
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    script {

                        def qg = waitForQualityGate(abortPipeline: false)

                        if (qg.status != 'OK') {
                            error "Pipeline aborted because Quality Gate failed: ${qg.status}"
                        }

                        echo ""
                        echo "======================================"
                        echo "SONARQUBE QUALITY GATE PASSED"
                        echo "======================================"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                set -e

                echo "===== Building Docker Image ====="

                docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} \
                    -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} \
                    -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:latest \
                    -f backend/Dockerfile \
                    backend
                '''
            }
        }
        stage('Trivy Image Scan') {
            steps {
                sh '''
                set -e

                echo "=================================="
                echo "TRIVY IMAGE SECURITY SCAN"
                echo "=================================="

                trivy image \
                    --severity HIGH,CRITICAL \
                    --no-progress \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
        stage('Azure Login') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'azure-acr',
                        usernameVariable: 'AZURE_CLIENT_ID',
                        passwordVariable: 'AZURE_CLIENT_SECRET'
                    )
                ]) {

                    sh '''
                    set -e

                    echo "===== Azure Login ====="

                    az login \
                        --service-principal \
                        -u $AZURE_CLIENT_ID \
                        -p $AZURE_CLIENT_SECRET \
                        --tenant b39b5cae-d7a4-4c51-a131-f33d7b6fa7f9

                    az acr login --name ${ACR_NAME}
                    '''
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                sh '''
                set -e

                echo "===== Push Docker Images ====="

                docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy to AKS') {
            steps {
                sh '''
                set -e

                echo "=================================="
                echo "DEPLOYING TO AZURE AKS"
                echo "=================================="

                kubectl config current-context

                kubectl set image deployment/${DEPLOYMENT_NAME} \
                    backend=${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} \
                    -n ${K8S_NAMESPACE}

                kubectl rollout status deployment/${DEPLOYMENT_NAME} \
                    -n ${K8S_NAMESPACE} \
                    --timeout=300s

                kubectl get pods -n ${K8S_NAMESPACE}
                '''
            }
        }
        stage('Application Smoke Test') {
            steps {
                sh '''
                set -e

                echo "=================================="
                echo "APPLICATION SMOKE TEST"
                echo "=================================="

                kubectl run smoke-test \
                    --rm -i \
                    --restart=Never \
                    --namespace ${K8S_NAMESPACE} \
                    --image=curlimages/curl:latest \
                    -- curl http://${SERVICE_NAME}/api/profile

                echo ""
                echo "=================================="
                echo "APPLICATION IS HEALTHY"
                echo "=================================="
                '''
            }
        }
        stage('Verify Deployment') {
            steps {
                sh '''
                echo ""
                echo "===== Kubernetes Context ====="

                kubectl config current-context

                echo ""
                echo "===== Pods ====="

                kubectl get pods -n ${K8S_NAMESPACE} -o wide

                echo ""
                echo "===== Deployment ====="

                kubectl get deployment ${DEPLOYMENT_NAME} \
                    -n ${K8S_NAMESPACE}

                echo ""
                echo "===== Services ====="

                kubectl get svc -n ${K8S_NAMESPACE}

                echo ""
                echo "===== Ingress ====="

                kubectl get ingress -n ${K8S_NAMESPACE}

                echo ""
                echo "===== Nodes ====="

                kubectl get nodes
                '''
            }
        }
        stage('List Docker Images') {
            steps {
                sh '''
                echo "===== Local Docker Images ====="

                docker images
                '''
            }
        }
    }

    post {

        success {

            echo '''

==============================================================
          ENTERPRISE ZERO-DOWNTIME CI/CD SUCCESS
==============================================================

✓ Source Code Checked Out

✓ Build Environment Verified

✓ SonarQube Analysis Completed

✓ Quality Gate Passed

✓ Docker Image Built

✓ Image Pushed to Azure Container Registry

✓ Kubernetes Deployment Updated

✓ Rollout Successful

✓ Health Check Passed

✓ Deployment Verified

==============================================================

'''
        }

        failure {

            sh '''
            echo "===== Kubernetes Debug ====="

            kubectl get pods -n enterprise || true

            echo ""
            kubectl describe deployment enterprise-backend \
                -n enterprise || true

            echo ""
            kubectl logs deployment/enterprise-backend \
                -n enterprise || true
            '''

            echo '''

==============================================================
                  PIPELINE FAILED
==============================================================

'''
        }

        always {

            cleanWs()

            sh '''
            docker system prune -af --volumes || true

            az logout || true
            '''
        }
    }
}
