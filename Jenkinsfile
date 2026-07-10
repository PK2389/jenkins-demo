pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Build') {
            steps {
                echo 'Building AWS Application...'
                sh 'python3 -m py_compile app.py test_app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'python3 -m unittest discover -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
            }
        }
    }
}