pipeline {
    agent any

    environment {
        IMAGE_NAME = "enterprise-backend"
        IMAGE_TAG = "${BUILD_NUMBER}"
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
                    echo "========== System Information =========="
                    whoami
                    pwd

                    echo "========== Java =========="
                    java -version || true

                    echo "========== Docker =========="
                    docker --version
                    docker ps

                    echo "========== Workspace =========="
                    ls -la
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
                      -f backend/Dockerfile \
                      backend
                '''
            }
        }

        stage('List Docker Images') {
            steps {
                sh '''
                    docker images
                '''
            }
        }
    }

    post {

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }

        always {
            cleanWs()
        }
    }
}
