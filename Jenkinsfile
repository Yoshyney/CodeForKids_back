pipeline {
    agent {
    docker {
 image 'python:3.7' 
}
 }
    stages {
        stage('Build') {
            steps {
          sh   'export PYTHONPATH=$PATH_TO_MODULE:$PYTHONPATH'
          sh  'pip install -r requirements.txt'
                echo 'Building..'
            }
        }
     }
        stage('Test') {
            steps {
            sh 'python hello.py'
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
