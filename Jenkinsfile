pipeline {
    agent any

    environment {
        IMAGE_NAME = "enterprise-backend"
        ACR_NAME = "ragulm175acr"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    tools {
        sonarQube 'SonarScanner'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ragulnn/enterprise-zero-downtime-cicd.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Local-SonarQube') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=enterprise-zero-downtime-cicd \
                      -Dsonar.sources=backend \
                      -Dsonar.python.version=3.12
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                  -t enterprise-backend:${BUILD_NUMBER} \
                  -f backend/Dockerfile \
                  backend
                '''
            }
        }

        stage('Docker Images') {
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
