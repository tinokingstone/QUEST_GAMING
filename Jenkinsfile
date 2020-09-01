  
pipeline{
        agent any
        stages{
            stage('test petclinic services'){
                steps{
                      sh """
                      ssh -i ~/id_rsa app-dev@51.145.17.150 <<EOF
                      rm -rf QAProject3
                      git clone --single-branch --branch stef-develop https://github.com/the-ci-squad/QAProject3
                      cd QAProject3/petclinic/spring-petclinic-backend/spring-petclinic-rest/
                      mvn test
                       """
                }
             }
             stage('launch petclinic'){
                steps{
                      sh """                  
                      ssh -i ~/id_rsa app-dev@51.145.17.150 <<EOF
        
                      rm -rf QAProject3
                      git clone --single-branch --branch stef-develop https://github.com/the-ci-squad/QAProject3
                      sudo apt install -y kubectl
                      sudo az aks install-cli
                      cd QAProject3/petclinic/kubernetes-petclinic
                      kubectl apply -f api.yml
                      kubectl apply -f front.yml
                      kubectl scale deployments/api --replicas=3 
                      kubectl scale deployments/front --replicas=3
                   
 
                 
                      """
               }
            }
        }    
}
