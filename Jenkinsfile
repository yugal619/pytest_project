pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yugal619/pytest_project.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv virtualenv
                . virtualenv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . virtualenv/bin/activate
                pytest
                '''
            }
        }
    }
}
