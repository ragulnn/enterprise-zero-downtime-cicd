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
                echo "===== Environment ====="

                whoami
                pwd

                docker --version
                kubectl version --client
                kubectl config current-context

                az --version

                echo ""
                echo "===== Kubernetes Nodes ====="

                kubectl get nodes
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

        stage('Build Docker Image') {
            steps {
                sh '''
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
                echo "===== Push Docker Images ====="

                docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                echo "===== Deploying ====="

                kubectl set image deployment/${DEPLOYMENT_NAME} \
                backend=${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} \
                -n ${K8S_NAMESPACE}

                kubectl rollout status deployment/${DEPLOYMENT_NAME} \
                -n ${K8S_NAMESPACE} \
                --timeout=180s
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "===== Pods ====="

                kubectl get pods -n ${K8S_NAMESPACE}

                echo ""

                echo "===== Deployment ====="

                kubectl describe deployment ${DEPLOYMENT_NAME} \
                -n ${K8S_NAMESPACE}

                echo ""

                echo "===== Service ====="

                kubectl get svc -n ${K8S_NAMESPACE}

                echo ""

                echo "===== Endpoints ====="

                kubectl get endpoints ${DEPLOYMENT_NAME} \
                -n ${K8S_NAMESPACE}
                '''
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {

        success {
            echo '''
==========================================
 PIPELINE COMPLETED SUCCESSFULLY
==========================================

Application Built
Docker Image Created
Image Pushed to ACR
Deployment Updated
Rollout Successful

==========================================
'''
        }

        failure {
            sh '''
            echo "===== Deployment Debug ====="

            kubectl get pods -n enterprise || true

            kubectl describe deployment enterprise-backend -n enterprise || true
            '''

            echo "Pipeline Failed"
        }

        always {
            cleanWs()

            sh '''
            docker image prune -f || true
            '''
        }
    }
}
