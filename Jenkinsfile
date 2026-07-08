pipeline {
    agent any

    options {
        // Keep the last 10 builds and time out a stuck run after 30 minutes.
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 30, unit: 'MINUTES')
        timestamps()
    }

    environment {
        APP_NAME = 'jenkins-demo'
        // Short git SHA makes a handy, unique build/version tag.
        BUILD_VERSION = "${env.BUILD_NUMBER}-${GIT_COMMIT.take(7)}"
        CI = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Building ${APP_NAME} version ${BUILD_VERSION}"
                checkout scm
            }
        }

        stage('Install') {
            steps {
                echo 'Installing dependencies...'
                // Use a clean, reproducible install from package-lock.json.
                sh 'npm ci'
            }
        }

        stage('Lint') {
            steps {
                echo 'Linting...'
                sh 'npm run lint --if-present'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'npm test'
            }
            post {
                always {
                    // Publish JUnit-style results if your test tool produces them,
                    // e.g. jest-junit writing to junit.xml.
                    junit testResults: 'junit.xml', allowEmptyResults: true
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'npm run build --if-present'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying ${APP_NAME} ${BUILD_VERSION}..."
                // Replace with your real deploy command, e.g. a script or CD trigger.
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded for ${APP_NAME} ${BUILD_VERSION}."
        }
        failure {
            echo "Pipeline FAILED for ${APP_NAME} ${BUILD_VERSION}."
        }
        always {
            echo 'Cleaning up workspace.'
            cleanWs()
        }
    }
}
