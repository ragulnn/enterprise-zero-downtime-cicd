pipeline {
    agent any

    environment {
        IMAGE_NAME = "enterprise-backend"
        IMAGE_TAG = "${BUILD_NUMBER}"
        ACR_NAME = "ragulm175acr"
        ACR_LOGIN_SERVER = "ragulm175acr.azurecr.io"
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
                whoami
                docker --version
                kubectl version --client
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

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                -t ${IMAGE_NAME}:${IMAGE_TAG} \
                -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} \
                -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:latest \
                -f backend/Dockerfile \
                backend
                '''
            }
        }

        stage('Login to Azure Container Registry') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'azure-acr',
                    usernameVariable: 'AZURE_CLIENT_ID',
                    passwordVariable: 'AZURE_CLIENT_SECRET'
                )]) {
                    sh '''
                    az login --service-principal \
                      -u $AZURE_CLIENT_ID \
                      -p $AZURE_CLIENT_SECRET \
                      --tenant b39b5cae-d7a4-4c51-a131-f33d7b6fa7f9

                    az acr login --name ${ACR_NAME}
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/enterprise-backend \
                backend=${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} \
                -n enterprise

                kubectl rollout status deployment/enterprise-backend \
                -n enterprise --timeout=180s

                kubectl get pods -n enterprise
                '''
            }
        }

        stage('List Images') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
