# Software Engineering Challenge
Challenge for selecting Software engineers.

To complete this challenge you will need to:
- Create a Django application.
- Deploy it on GCP using Terraform.
- Implement CI pipelines for both Django and Terraform.

## API development
### Description
They have been always here, but we have never seen them. This API will be used by the Human Air Forces to defend the world against the alian invasion.

The API needs to have three entities:
- Mothership {ship capacity: 9}
- Ship {crew member capacity: 5}
- CrewMember

Mothership has many ships.
Ships has Mana CrewMembers.
### Requeriments
- Python ^3.9
- Poetry ^1.1.12
- Django ^3.2.12
### Acceptance criteria
- Given that the officer wants to add a mothership, when he adds a mothership, then the mothership will be created with three ships
- Given that the mothership was created, when the ship is created, then ship will create three crew members
- Given that the officer wants to add a ship to a mothership, when he sends which mother ship and how much ships he wants to add, then ships will be created with three crew members each one if the mothership contains less than 9 ships
- Given that the officer wants to remove a ship, when he tries he send which ship he wants to remove, then the ship will will be removed only if the ship has no crew members
- Given that the officer wants to add a crew member, when he sends the name of the member and the ship he wants to add, then the crew member is added if the ship contains less than 5 crew members
- When that the officer tries to add more ships or crew members than the capacities, then an error is raised pointing out what is wrong
- Given that the officer wants to switch a crew member between the ships, when he sends the from_ship and the to_ship and the name of the crew member, then the action will be allowed only if the from_ship will not remain with no crew members and the to_ship will not exceed the capacity
### Definition of Done
Complete the following checklist
1. Use the [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide) as reference
2. Remove duplicated or unnecessary code
3. Avoid hardcoded values
4. No unnecessary comments
5. Unit test implemented checking custom behaviors and business rules
6. API Documentation
    1. Action | route
    2. Description
    3. URL Parameters
    4. Request Params
    5. Request body
    6. Response body
    7. Status code

## Terraform
### Acceptance Criteria
- Deploy API.
- Make API reachable from internet using Load Balancer.
- Deploy Database.
- If you need any service account in the API give it the least privileges possible.
- Use terraform to deploy your application on GCP.
- You can use any GCP service you want, but would be a bonus if you use CloudRun.
- Migrations should run using automation.
- Create docker-compose to make it easy to run the application locally (it should include the api container).
- Test your terraform code using terratest.
- Build CI pipeline using Github Actions to run terratest.

### Definition of Done
Complete the following checklist
1. Use Terraform latest version.
2. Use terraform fmt to style the code.
3. Remove any unused variables.
4. Remove any unused resources.
5. No code replication.
6. No hardcoded values.
7. Use Golang latest version.
