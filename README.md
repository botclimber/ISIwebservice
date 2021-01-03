# ISIwebservice
## ISI - project - RESTful web service

### Context

This is an api service to manage a recipes db. The functionalities are:
- CREATE recipe or Ingredient
- UPDATE recipe or Ingredient
- DELETE recipe or Ingredient
- GET recipe or Ingredient:
	- GET all
	- GET one by id
	- GET random (only in recipes)

## Usage
### if locally
After clone it, install requirementes by running following command:
```
pip3 install -r requirements.txt
```
then just run:
```
python3 main.py
```
and u can start using it. first page will be the api documentation:
![Image of api_doc](https://github.com/botclimber/ISIwebservice/static/img/api_doc.png)

## Functionalities:

* api info:
	- [ ] api documentation incomplete

* Auth:
	- [x] create and send user apiKey done
	- [x] generic method to verifications done

* recipes:
	- [x] get all recipes done
	- [x] get recipe by id done
	- [x] get random recipe functionality done 
	- [x] create recipe functionality done
	- [x] update recipe functionality done
	- [x] delete recipe functionality done

* Ingredients:
	- [x] get all ingredients done 
	- [x] get ingredient by id done
	- [x] create ingredient done
	- [x] update ingredient done
	- [?] delete ingredient undone

* performance & usage:
	- [x] method to verify id id exists at any class
	- [ ] simplify code
	- [ ] document code | classes signature
	- [x] script to install all dependencies at one
