pipeline{
    agent any

    enviorment {
        DOCKERHUB_CREDENTIALS=credentials('sajjad-docker-login')
    }

    stages{

        stage("gitclone") {

            steps {
                echo 'git clone the application' 
                git 'https://github.com/sajjadp/myapp.git'
            }
        }
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
    }
    post {
        always{
            sh 'docker logout'
        }
    }
}