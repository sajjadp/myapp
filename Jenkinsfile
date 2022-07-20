pipeline{
    agent {label 'ubuntu'}

    environment {
        DOCKERHUB_CREDENTIALS=credentials('sajjad-docker-login')
    }

    stages{

        stage("build") {
            steps {
                echo 'docker image building'
                sh 'docker build -t sajjadp/newapp:latest .' 

            }
        }
        stage ("login"){
            steps {
                echo 'login in docker hub'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage ('push') {
            steps {
                echo 'pushing the image to dockerhub'
                sh 'docker push sajjadp/newapp:latest'
            }
        }
        stage ('run docker app') {
            steps {
                echo 'runnnig the docker app'
                sh ' docker run -d -p 8080:8080 sajjadp/newapp'
            }
        }
        
    }
    post {
        always{
            sh 'docker logout'
        }
    }
}