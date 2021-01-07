# ISIwebservice
## ISI - project - RESTful web service

### Context

This is an api that provides info about recipes and ingredients, the user can create his own recipes and manage them, also this gives information about beers and it is related with recipes functionality. The beers information comes from an external api.

## Usage
### if locally
After clone it, install requirementes by running following command:
```
pip3 install -r requirements.txt
```
then just run:
``` 
python3 main.py (recomended)
``` 
or
```
flask run
```

and u can start using it. first page will be the api documentation:
![Image of api_doc](https://github.com/botclimber/ISIwebservice/blob/main/static/img/api_img.png)

## Functionalities:
* Client:
	- in progress ...

* api info:
	- [x] api documentation complete
	- [ ] update auth to return token instead	
	- [ ] make it a litle more intuitive

* Auth:
	- [x] create user done
	- [x] login done
	- [x] use JWT to auth functionalities done
	- [ ] give common user permission to manage recipes

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
	- [?] update ingredient done
	- [?] delete ingredient undone

* Beers: [data from external api]
	- [x] get all beers done
	- [x] get beer details done
	- [x] get random beer done
	- [x] recomend beer to pair food done

* security:
	- [ ] regist every request (ip, type of, user, datetime) undone

* performance & usage:
	- [x] method to verify if id exists at any class
	- [ ] simplify code
	- [ ] document code | classes signature
	- [x] script to install all dependencies at one
