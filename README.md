# Software Engineering Challenge
Challenge for selecting Software engineers.

To complete this challenge you will need to:
- Create a Django application.
- Deploy it on GCP using Terraform.
- Implement CI pipelines for both Django and Terraform.

## Requeriments
### API
They habe been always here, but we have never seen them. This API will be used by the Human Air Forces to defend the world against the alian invasion.

- Mothership
- Ship
- CrewMember

Mothership has many ships.
Ships has Mana CrewMembers.
### Terraform

## Acceptance criteria
Using the template Given/When/Then describe clearly which behaviors are being expected.
- The frontend wants to change the php settings then they will send a request to the route `apps/<app_id>/settings` with the request body and then they will receive an operation_id.
## Definition of Done
Complete the following checklist
1. check the code (technical review)
2. Use the [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide) as reference
3. Remove duplicated or unnecessary code
4. Avoid hardcoded values
5. No unnecessary comments
6. Sufficient logging with proper logger
7. Unit test implemented checking custom behaviors and business rules
8. Update a ENDPOINTS.md file describing (If applicable)
    1. Django app name
    2. Action | route
    3. TAG: Draft | Publish
    4. Description
    5. URL Parameters
    6. Request Params
    7. Request body
    8. Response body
    9. Status code

