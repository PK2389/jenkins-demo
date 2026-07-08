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
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Building ${APP_NAME} version ${BUILD_VERSION}"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Replace with your real build command, e.g.:
                // sh 'make build'  or  sh './gradlew assemble'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Replace with your real test command, e.g.:
                // sh 'make test'  or  sh './gradlew test'
            }
            post {
                always {
                    // Publish JUnit-style results if your test tool produces them.
                    // junit 'build/test-results/**/*.xml'
                    echo 'Test stage complete.'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying ${APP_NAME} ${BUILD_VERSION}..."
                // Replace with your real deploy command.
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
