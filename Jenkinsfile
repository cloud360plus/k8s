pipeline {
    agent any

    environment {
        IMAGE = "dockerhub_username/app:${BUILD_NUMBER}"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/cloud360plus/k8s.git'
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        sh '''
                        docker build -t $IMAGE .
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker push $IMAGE
                        '''
                    }
                }
            }
        }

        stage('Update K8s Manifest & Push to Git') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'git-creds', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                    script {
                        sh '''
                        sed -i "s|image:.*|image: $IMAGE|" k8s/deployment.yaml
                        git config --global user.email "santoshgupta022@gmail.com"
                        git config --global user.name "$GIT_USERNAME"
                        git add k8s/deployment.yaml
                        git commit -m "CI: Update image to $IMAGE"
                        git push https://$GIT_USERNAME:$GIT_PASSWORD@github.com/your-username/your-repo.git HEAD:main
                        '''
                    }
                }
            }
        }
    }
}
