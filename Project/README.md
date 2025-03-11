# Unit 3: Online Food Order Platform
![giphy](https://github.com/user-attachments/assets/a94eed6a-dc3e-49b3-b079-c3d39c76a7a1)


<sub>gif by @E3maly on GIPHY, https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHZlODlrNDJlOXE3a3RrNzg4MzUzOTJ1NWhqbWFmY2p5ZzhybXQ5ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iUaDOqormK0U5yEdRT/giphy.gif</sub>

## Criterion A: Planning

### Problem definition
“The Good Old Times” (in this document referred to as TGOT) is a new business that lets an international boarding school’s students buy international and traditional food from all over the world, with the mission to tackle students’ homesickness and make them feel more comfortable on campus. However, the founder has expressed difficulties accessing these foods because the school is located in a relatively remote area. As a result, she wishes to implement some sort of online platform that showcases all the products and allows students to order them by selecting them to solve this problem. 

There are also other issues stemming from the main problem. As of current, students in this school often mistaken other students’ packages as theirs, and some even take others’ deliveries on purpose. Hence, the founder of TGOT wishes for a way to identify these students when they are paying on delivery when the packages arrive. The information students are willing to share are their emails and names (both first and last name), but it would be better if the identification process is more simple and secure instead of entering phone numbers every time. Moreover, the students would need to be notified when packages are delivered because food has a short expiry date. 

Another problem is that some students have dietary restrictions such as halal or vegetarian, therefore the founder would like students to have access to the detailed information on each product. And due to students’ limited budgets, they should be able to double check their total spending before they confirm the order. 

_*see evidence of consultation in the Appendix_


### Proposed Solution
Python, a higher level and interpreted programming language is selected as this project's main programming language. This is because Python has a huge selection of third party modules and library, my other tool kivymd being one of them. 

### Success Criteria
1. The application includes a log-in/registration system to identify students. 
    - [Issue tackled: “students in this school often mistaken other students’ packages as theirs, and some even take others’ deliveries on purpose”, “but it would be better if the identification process is more secure”]

2. The application showcases all the products prepopulated in the main page clearly with an option for the items to be selected by clicking on the image
    - [Issue tackled: “she wishes to implement some sort of online platform that showcases all the products and allows students to order them by selecting them”]

3. Once a product is selected, a new window opens with a detailed description (allergens, ingredients, restrictions, country of origin) and picture of the product, with the option to add it to their cart. 
    - [Issue tackled: “Another problem is that some students have dietary restrictions such as halal or vegetarian, therefore the founder would like students to have access to the detailed information on each product”]

4. The application allows users to save the product to cart to confirm order for later, and upon clicking the cart icon, a page would showcase the total cost of the order with a confirm button that confirms the order.
    - [Issue tackled: “And due to students’ limited budgets, they should be able to double check their total spending before they confirm the order.”]

5. When the package is ordered, a pop up notification would appear on the screen of the user to inform them of the estimated arrival time.  
    - [Issue tackled: “Moreover, the students would need to be notified when packages are delivered because food has a short expiry date.”]

## Criterion B: Design

### System Diagram
![Untitled Diagrameqzx drawio](https://github.com/user-attachments/assets/74b033dc-6f2d-45fb-bdfe-e9e1a9ee54fc)


**Fig. 1** This is the system diagram of the proposed solution. 


### Flow diagrams for algorithms


![flowchart1 drawio](https://github.com/user-attachments/assets/a21acc40-6466-453f-b0b9-92f5e68e789e)

**Fig. 2** This is the flow diagram for try_login() which attempts log in for the information entered in the text field


![flowchart2 drawio](https://github.com/user-attachments/assets/5663e568-6449-40c5-81ac-2214a9482856)

**Fig. 3** This is the flow diagram for load_cart_items() which displays all the items in the cart of a user


![flowchart3 drawio](https://github.com/user-attachments/assets/50cfb862-1723-4c94-9cfc-ecbd2ede3be2)

**Fig. 4** This is the flow diagram for confirm() which confirms the order and shows in how many days the product would arrive

### UML Diagram (Object Oriented Programming)
![P3_UML drawio](https://github.com/user-attachments/assets/613f94cf-31f8-42c3-b3c6-ce59678f75f0)

**Fig.5** UML diagram of the classes in the application

### ER Diagram (Databases) 
![Untitled Diagram drawio](https://github.com/user-attachments/assets/107dc6cb-f412-430e-bc1a-4def26339d7a)

**Fig.6** ER diagram of the database


### Tables
The database is named login.sql by accident, and due to issues with Pycharm's setup, it's too late to change the name. I would have named it app.sql. 
![image](https://github.com/user-attachments/assets/242435fd-3ffc-4ab5-8dde-1aa883bf4ba2)

**Fig.7** table "products" in login.sql in the database




![image](https://github.com/user-attachments/assets/e856ec6b-bdfb-4b19-96a8-46320469c251)

**Fig.8** table "user" in login.sql in the database (the first row was a debugging result)





![image](https://github.com/user-attachments/assets/221d458d-6256-4b45-a4cb-17c5cf1a3743)

**Fig.9** table "cart_orders" in login.sql in the database. The table is empty right now because no orders have been made in the application. 





### wireframe diagram (User Interface)
none for now

### Test plan
| Success Criteria Addressed                                                                                                                                                                                                | Purpose                                                                            | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Expected Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. The application includes a log-in/registration system to identify students.                                                                                                                                            | Check whether the log in/sign up system works properly                             | 1. Run the application. <br>2. Press "Log in" button without inputting anything into any text fields on the screen.  <br>3. Input "jinx" in the username field and "4rc4n3" as password and press "Log in" button. <br>4. Press "Don't have an account? Sign up here" and click "Sign up" button without inputting anything into any text fields on the screen. <br>5. Input "user{a number of your choice}" in the username field and "{that number of your choice}" in the email field, and input 123123 in the create password field, and 123123 in the confirm password field. Press the "Sign up" button. <br>6. Change the input in the email field to "{that number of your choice}@gmail.com", and change the input in the create password field to 321321. Press the "Sign up" button. <br>7. Change the input in the create password field to 123123, then change the input in the email field to "hehehehaw@gmail.com". Press the "Sign up" button.<br>8. Change the input in the email field back to "{that number of your choice}@gmail.com". Press the "Sign up" button. <br>9. Input "user{that number of your choice}" in the username field and 123123 in the password field. Press the "Log in" button. <br>10. On the bottom of the home screen, click the icon with the text "Profile". <br>11. On the profile page, click the button "Log out". | 1. A phone sized screen appears, showing a log in page. <br>2. Red hint texts under each text fields appear, showing text "please enter a username"/"please enter a password". <br>3. Red hint text under the username field appears showing text "invalid username or password". <br>4. User is redirected to the sign up interface then red hint text under the username field appears showing text "all information needs to be filled out". <br>5. Red hint text under the email field appears showing text "email is not in correct format. please check again". <br>6. Red hint text under the password confirmation field appears showing text "passwords don't align. please check again". <br>7. Red hint text under the username field appears showing text "username or email already in use". <br>8. User is redirected back to the log in page with the text fields cleared. <br>9. User is redirected to the home page. <br>10. User is redirected to the profile page with the text "Hello {current user's username}". <br>11. User is redirected back to the log  in page with the text fields cleared.                                                                                                                                                                                                                                                                                                                                                            |
| 2. The application showcases all the products prepopulated in the main page clearly with an option for the items to be selected by clicking on the image                                                                  | Check whether products are shown on the main page                                  | 1. Continue from success criteria 1's test, enter "Antek" in the username field, and "000000" in the password field. Press the "Log in" button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 1. User is redirected to home page, which has a scrollable view of cards containing the product's image, name, and price.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 3. Once a product is selected, a new window opens with a detailed description (allergens, ingredients, restrictions, country of origin) and picture of the product, with the option to add it to their cart.                                               | Check whether product information could be shown according to the product selected | 1. Continue from success criteria 2's test, click on one random product card. <br>2. Click the "Back" button on the screen.<br>3. Click on another product.<br>4. Click the "Back" button on the screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1. User is redirected to the product detail page of that product, with it's image, price, name, ingredients, allergens, dietary restrctions, and coutnry of origin shown on the screen. There are two buttons, one to go back to the home page, the other to add the item to the user's cart. <br>2. User is redirected back to the home page. <br>3. User is redirected to the product detail page of that product, with it's image, price, name, ingredients, allergens, dietary restrctions, and coutnry of origin shown on the screen. (The information on the page should be different that that of 1.) There are two buttons, one to go back to the home page, the other to add the item to the user's cart.<br>4. User is redirected back to the home page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 4. The application allows users to save the product to cart to confirm order for later, and upon clicking the cart icon, a page would showcase the total cost of the order with a confirm button that confirms the order. | Check whether the cart and order system functions properly                         | 1. Continue from success criteria 3's test, click on the product card named "Lao Gan Ma Chili Oil".<br>2. Press the "Add to your cart" button. <br>3. Click "Close" on the pop up dialogue.<br>4. Click the cart icon on the navigation bar. <br>5. Click home icon on the navigation bar and then click on the product card named "Peanut Mochi". <br>6. Press the "Add to your cart" button. <br>7. Click "Close" on the pop up dialogue.<br>8. Click the cart icon on the navigation bar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1. User is redirected to the product detail page of the chili oil, with it's image, price, name, ingredients, allergens, dietary restrctions, and coutnry of origin shown on the screen. There are two buttons, one to go back to the home page, the other to add the item to the user's cart.<br>2. A pop up dialogue shows up with the message informing the user that the item has been added to their cart with a "Close" button. <br>3. User is redirected back to the home page. <br>4. User is redirected to the cart page, and the chili oil's name "Lao Gan Ma Chili Oil" and price (795) appears in the scrollable view on the page. The total amount text shows 795. <br>5. User is redirected to the product detail page of the peanut mochi, with it's image, price, name, ingredients, allergens, dietary restrctions, and coutnry of origin shown on the screen. There are two buttons, one to go back to the home page, the other to add the item to the user's cart.<br>6. A pop up dialogue shows up with the message informing the user that the item has been added to their cart with a "Close" button.<br>7. User is redirected back to the home page.<br>8. User is redirected to the cart page, and the peanut mochi's name "Peanut Mochi" and price (565) appears in the scrollable view on the page under the chili oil. The total amount text shows 1360 (975+565).<br>9. The chili oil disappears from the list on the page, and the total is now 565. |
| 5. When the package is ordered, a pop up notification would appear on the screen of the user to inform them of the estimated arrival time.                                                                                | Check whether the product order confirm function works properly                    | 1. Continue from success criteria 4's test, click the "confirm" button.<br>2. Click the "Close" on the pop up dialogue. <br>3. Click the cart item on the navigation bar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1. A pop up dialogue shows up with the message informing the user that their order has been confirmed, and that it will arrive in {a random number between 2 and 12} days. <br>2. User is redirected back to the home page.<br>3. User is redirected to the cart page and the total is 0 and there are no items on the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |




### Record of Tasks
| **Planned action**                                      | **Planned outcome**                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Time estimate** | **Target completion date** | **Criteria** |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------|--------------|
| Interview the client for a description of the problem   | After listening to the client's description of the problem, I would finish writing the problem definition                                                                                                                                                                                                                                                                                                                                                                                 | 30 min            | Feb 4                      | A            |
| Meet with the client again to show the success criteria | After writing the definition of the problem, I would highlight the main issues and create success criterion based on them and check with the client                                                                                                                                                                                                                                                                                                                                       | 35 min            | Feb 7                      | A            |
| Research and propose a solution                         | Research methods and write a proposed solution based on the finalized success criteria and justify choice of tools and methods with citations                                                                                                                                                                                                                                                                                                                                             | 1 hr              | Feb 11                     | A            |
| Create design plan                                      | 1. Create a color scheme using Coolors and the logo for the application using Canva. <br>2. Find and download from Google fonts the font that is going to be used in the application. <br>3. Find and record the information of the example products sold on the application and note down their links for citation. <br>4. Download all images needed, process them as needed, and move them to this project's folder. <br>5. Note down relevent design information on a Google Document | 1 hr 30 min       | Feb 19                     | B            |
| Create diagrams for backend of the application          | Create a UML diagram, ER diagram, 3 flow diagrams - one simple, one medium, one hard, and a system diagram                                                                                                                                                                                                                                                                                                                                                                                | 3 hrs             | Feb 26                     | B            |
| Create a test plan                                      | Create a test plan table that provides instructions on input and expected output of the application matching the success criteria                                                                                                                                                                                                                                                                                                                                                         | 1 hr              | Feb 28                     | B            |
| Create the log in page user interface (UI)              | Code, using kivymd and some Python on Pycharm, the log in UI. It follows the design plan (color scheme, font, logo)                                                                                                                                                                                                                                                                                                                                                                       | 40 min            | Mar 1                      | C            |
| Create the sign up page UI                              | Code, using kivymd and some Python on Pycharm, the sign up UI by modifying the log in UI. It follows the design plan (color scheme, font, logo)                                                                                                                                                                                                                                                                                                                                           | 20 min            | Mar 1                      | C            |
| Create the home page UI                                 | Code, using kivymd and some Python on Pycharm, the home page UI that has a scrollable display of products and a navigation bar at the bottom. It follows the design plan (color scheme, font, logo, product information and price)                                                                                                                                                                                                                                                        | 1 hr              | Mar 1                      | C            |
| Create the product details page UI                      | Code, using kivymd and some Python on Pycharm, the product page UI. It follows the design plan (color scheme, font, product information and price)                                                                                                                                                                                                                                                                                                                                        | 1 hr              | Mar 2                      | C            |
| Create the profile page UI                              | Code, using kivymd and some Python on Pycharm, the profile page UI. It follows the design plan (color scheme, font, logo)                                                                                                                                                                                                                                                                                                                                                                 | 45 min            | Mar 2                      | C            |
| Develop the log in and sign up system                   | Code, using a database (SQLite) and Python on Pycharm, the functions of the log in and sign up system using the test plan as a reference to test it's functionality                                                                                                                                                                                                                                                                                                                       | 1 hr 30 min       | Mar 5                      | C            |
| Populate the products table                             | Using the SQLite console, populate the products table (already created in the Python code) with the relevent product information                                                                                                                                                                                                                                                                                                                                                          | 1 hr              | Mar 6                      | C            |
| Develop the product details system                      | Code, using Python on Pycharm, the functions of automatically updating the information of the products in the UI based on the contents in a table                                                                                                                                                                                                                                                                                                                                         | 1 hr 30 min       | Mar 7                      | C            |
| Create the cart page UI                                 | Code, using kivymd and some Python on Pycharm, the cart page UI. It follows the design plan (color scheme, font, logo, product information and price).                                                                                                                                                                                                                                                                                                                                    | 1 hr              | Mar 8                      | C            |
| Develop the cart system                                 | Code, using Python on Pycharm, the functions of adding items to the cart and showing items on the cart page UI based on the contents in a table for orders, showing the total after adding up the price, and clearing the table after user completes order                                                                                                                                                                                                                                | 1 hr              | Mar 8                      | C            |
| Develop the delivery time popup system                  | Code, using Python and some kivymd on Pycharm, the functions of randomizing the delivery time and showing it on a popup after order is confirmed. It follows the design plan (color scheme, font)                                                                                                                                                                                                                                                                                         | 1 hr              | Mar 8                      | C            |
| Debug and test run                                      | Run the application then test it using the instructions on the test plan table. Adjust the application as needed.                                                                                                                                                                                                                                                                                                                                                                         | 30 min            | Mar 9                      | C            |
| Refine test plan                                        | Refine the test plan after finishing the whole application and testing it out using the test plan, removing redundant parts and make the instructions more detailed and tailored to the application.                                                                                                                                                                                                                                                                                      | 30 min            | Mar 9                      | B            |
| Identify tools and techniques used                      | Identify the tools (packages and libraries) used and techniques used, list them out on the .md file.                                                                                                                                                                                                                                                                                                                                                                                      | 30 min            | Mar 9                      | C            |
| Review the code and explain it                          | Write down what each snippet of code does and explain it on the .md file                                                                                                                                                                                                                                                                                                                                                                                                                  | 3 hrs             | Mar 9                      | C            |
| Record the demonstration video                          | Record the demonstration video and in it, test the application using the test plan.                                                                                                                                                                                                                                                                                                                                                                                                       | 30 min            | Mar 11                     | D            |
| Finalize Record of Tasks table                          | Make sure everything is completed based on the record of tasks table                                                                                                                                                                                                                                                                                                                                                                                                                      | 30 min            | Mar 12                     | B            |





## Criterion C: Development

### Techniques used
- **If/else conditions statements**: Used to control actions based on certain conditions, for example in this application, validate user inputs and login credentials. 
- **For loops**: Used to iterate through items in the database. 
- **Functions**: Used to organize my code into reusable and callable blocks, which makes the code more organized and easier to debug and alter. Example functions in this application: add_to_cart(), try_register(). 
- **Classes (OOP)**: Used to structure the application, for example, the different screens (HomeScreen, CartScreen, etc.) in this application.
- **Hashing**: Used to store password securely in a database by encrypting it. 
- **Databases**: Allows data to be saved and retrieved when required. Used to store user information, product information, etc.

### Packages used
- SQLite3
- kivy
- kivymd
- passlib
- random

### User Interface
For the log-in and sign up page, I followed a tutorial[^6] for some parts of the layout, but added my personal fonts and color, and adjusted quite a lot of things to fit the theme I am going for. I followed another tutorial[^4] for the home page too, to figure out how scrollable view of cards could be achieved, and how a navigation bar could be made, but I also adjusted it a lot to fit my theme. 

### Success criteria 1: Log in/Sign up
Classes ```LoginScreen``` and ```SignupScreen``` are responsible for the log in and sign up systems. Both classes have a similar function that resets the text fields, as shown below, so that the previous user's information would not be on there when a new user attempts to sign up or log in to improve security and privacy.

```.py
    def on_pre_enter(self):
        Clock.schedule_once(self.clear_login, 0.01)
    def clear_login(self,placeholder):
        self.ids.password.text = ""
        self.ids.username.text = ""
```
For the log in screen, I clear it before the screen is displayed so the sensitive information wouldn't be seen.
```.py
    def on_enter(self):
    self.ids.pw1.text = ""
    self.ids.pw2.text = ""
    self.ids.signup_name.text = ""
    self.ids.signup_email.text = ""
```
However, for sign up screen, I clear it on the moment the screen is displayed because sign up has less sensitive information. 

For logging in, the main function, ```try_login()``` is activated upon the release of the log in button, and it checks whether a username is entered and whether a password is entered, then it checks for whether there exists such a user, then it checks whether the username matches the encrypted password. The way it checks whether there exists such a user and whether the username matches the encrypted password is by using the DatabaseManager class from my other file, mylib.py, to query for entries that match the username entered, and if that is equal to 1, it checks for whether the password of that entry decrypted using also another function from mylib.py match the one enntered. If all of the above conditions are met, then the user is led to the home page. 
```.py
    def try_login(self):
        username = self.ids.username.text
        password1 = self.ids.password.text
        if username == "":
            self.ids.username.helper_text = "please enter a username"
        else:
            self.ids.username.helper_text = ""
        if password1 == "":
            self.ids.password.helper_text = "please enter a password"
        else:
            self.ids.password.helper_text = ""
        if password1 and username:
            query = f"SELECT * FROM user WHERE username = '{username}'"
            db = DatabaseManager(name="login.sql")
            result = db.search(query)
            if len(result) == 1:
                hash_column = 3
                hash = result[0][hash_column]
                if check_password(hash, password1):
                    LoginScreen.current_user = username
                    self.parent.current = "HomeScreen"
                else:
                    self.ids.password.helper_text = "incorrect password"
            else:
                self.ids.username.helper_text = "invalid username or password"

    def switch_to_signup(self):
        self.parent.current = "SignupScreen"
```
(MyApp.py)
```.py
import sqlite3
from passlib.context import CryptContext
from random import randint

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000)

def encrypt_password(user_password):
    return pwd_config.hash(user_password)

def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

def random_days():
    return randint(2,12)

class DatabaseManager:
    def __init__(self, name: str):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def close(self):
        self.connection.close()


    def run_save(self,query):
        self.cursor.execute(query)
        self.connection.commit()
```
(mylib.py)
```.kv
<LoginScreen>:
    MDScreen:
        MDFloatLayout:
            md_bg_color: "#e4ccb0"
            Image:
                source: "logo-clear.png"
                pos_hint: {"center_x":.22, "center_y": .85}
                size_hint: .5,.5
            MDLabel:
                text: "Welcome back!"
                color: "#6a5750"
                font_size: 40
                font_name: "Lora.ttf"
                pos_hint: {"center_x":.6, "center_y": .70}
            MDLabel:
                text: "Log in"
                bold: True
                color: "#210d02"
                font_size: 50
                font_name: "Lora.ttf"
                pos_hint: {"center_x":.6, "center_y": .63}

            MDFloatLayout:
                size_hint: .85,.08
                pos_hint: {"center_x":.52, "center_y": .48}

                MDLabel:
                    text: "Username"
#                    font_name: "Lora.ttf"
                    font_size: "12sp"
                    pos_hint: {"center_x": .5, "center_y": .95}
                    theme_text_color: "Custom"
                    text_color: "#6a5750"

                MDTextField:
                    id: username
                    font_name_helper_text: "Lora.ttf"
                    font_name: "Lora.ttf"
                    helper_text_color_normal: "#ad2923"
                    mode: "line"
                    helper_text: ""
                    helper_text_mode: "persistent"
                    size_hint_x: 0.9
                    pos_hint: {"center_x": .45, "center_y": .5}
                    foreground_color: "#210d02"
                    hint_text_color_focus: "#6a5750"
                    line_color_focus: "#6a5750"
                    icon_right: "account"

            MDFloatLayout:
                size_hint: .85,.08
                pos_hint: {"center_x":.52, "center_y": .35}

                MDLabel:
                    text: "Password"
#                    font_name: "Lora.ttf"
                    font_size: "12sp"
                    pos_hint: {"center_x": .5, "center_y": .95}
                    theme_text_color: "Custom"
                    text_color: "#6a5750"

                MDTextField:
                    id: password
                    font_name: "Lora.ttf"
                    helper_text_color_normal: "#ad2923"
                    helper_text: ""
                    helper_text_mode: "persistent"
                    mode: "line"
                    password: True
                    size_hint_x: 0.9
                    pos_hint: {"center_x": .45, "center_y": .5}
                    foreground_color: "#210d02"
                    hint_text_color_focus: "#6a5750"
                    line_color_focus: "#6a5750"
                    icon_right: "key"

            MDFlatButton:
                id: login_btn
                text: "[color=#f8e2ca]Log in[/color]"
                md_bg_color: "#8b5742"
                text_color: "#f8e2ca" #fsr this doesn't work?????
                font_name: "Lora.ttf"
                size_hint: .79, .08
                pos_hint: {"center_x": .48, "center_y": .21}
#                line_color: "#6a5750"
#                line_width: 2
                on_release: root.try_login()
            MDTextButton:
                text: "Don't have an account? Sign up here"
#                font_name: "Lora.ttf"
                font_size: "12sp"
                pos_hint: {"center_x": .48, "center_y": .12}
                halign: "center"
                on_press: root.switch_to_signup()
```
(MyApp.kv)

For signup, there are more checks, which are pretty self explanatory looking at the comments. When all coniditions are met, the user's information is added to the user table and the user is then led to the log in page to log in with their newly created account. 
```.py
    def switch_to_login(self):
        self.parent.current = "LoginScreen"

    def try_register(self):
        username = self.ids.signup_name.text
        email = self.ids.signup_email.text
        pw1 = self.ids.pw1.text
        pw2 = self.ids.pw2.text

        # 3/ check if the field is not empty
        if username == "" or pw1 == "" or pw2 == "" or email == "":
            # self.ids.signup_name.error = True
            self.ids.signup_name.helper_text = "all information needs to be fill out"
        else:
            self.ids.signup_name.helper_text = ""
            #validation
            #1/ is user and password unique?
            check1_query = f"SELECT * from user where username = '{username}' or email = '{email}'"
            db =  DatabaseManager(name="login.sql")
            results = db.search(query=check1_query)
            db.close()


            if len(results)>0:
                #user or email already used
                # self.ids.signup_name.error = True
                self.ids.signup_name.helper_text = "username or email already in use"
                return
            else:
                self.ids.signup_name.helper_text = ""

            if " " in username:
                #user or email already used
                # self.ids.signup_name.error = True
                self.ids.signup_name.helper_text = "username cannot contain spaces"
                return
            else:
                self.ids.signup_name.helper_text = ""

            # 4/ check if email has the @ mark
            if "@" not in email or "." not in email:
                # self.ids.signup_name.error = True
                self.ids.signup_email.helper_text = "email is not in correct format. please check again"
                return
            else:
                self.ids.signup_email.helper_text = ""

            #2/does password match?
            if pw1 != pw2:
                # self.ids.signup_password.error = True
                self.ids.pw2.helper_text = "passwords don't align. please check again"
                return
            else:
                self.ids.pw2.helper_text = ""



            hashed_pw = encrypt_password(pw1)
            db1 = sqlite3.connect("login.sql")
            c = db1.cursor()
            insert_query = "INSERT INTO user (username, email, password) VALUES (?,?,?)"
            c.execute(insert_query, (username, email, hashed_pw))
            db1.commit()
            c.close()

            self.parent.current = "LoginScreen"
```
(MyApp.py)

### Success criteria 2 & 3: displaying products and individual product details. 
The home screen shows all the products in cards in a scrollable view. The class HomeScreen contains a function for the card in the scrollable view: when the card is clicked on, the prd_id (product id) of it is passed onto the ProductDetails class to retrieve information from the database using the prd_id, displaying the detailed information (country of origin, ingredients... etc.) of the product in the product details page. 
```.py
class HomeScreen(Screen):

    def goto_product(self, image, p_name, price,prd_id):
        product_screen = self.parent.get_screen("ProductDetail")
        product_screen.image = image
        product_screen.p_name = p_name
        product_screen.price = price
        product_screen.prd_id = prd_id
        self.parent.current = "ProductDetail"
```
This function passes the image, product name, price, and product id to ProductDetail, the page that shows the detailed information of the products. This means that I don't need to create a separate detail page for each product, instead, i could just create one, and substitute the values of different products into it .

```.kv
        ScrollView:
            MDGridLayout:
                cols: 2
                spacing: 40
                padding: 5
                size_hint_y: None
                height: self.minimum_height
                adaptive_height: True
                ProductCard:
                    prd_id: "cake"
                    image: "products/cake.png"
                    price: "325¥"
                    p_name: "Taiwanese Style Cake"

                ProductCard:
                    prd_id: "mochi"
                    image: "products/mochi.png"
                    price: "565¥"
                    p_name: "Peanut Mochi"

                ProductCard:
                    prd_id: "pho"
                    image: "products/pho.png"
                    price: "260¥"
                    p_name: "Instant Pho Beef Flavor"

                ProductCard:
                    prd_id: "laoganma"
                    image: "products/laoganma.png"
                    price: "795¥"
                    p_name: "Lao Gan Ma Chili Oil"


                ProductCard:
                    prd_id: "shinramyun"
                    image: "products/shinramyun.png"
                    price: "260¥"
                    p_name: "Shin Ramyun (spicy)"

                ProductCard:
                    prd_id: "ricecake"
                    image: "products/ricecake.png"
                    price: "860¥"
                    p_name: "Tteokbokki Rice Cake"



                ProductCard:
                    prd_id: "cracker"
                    image: "products/cracker.png"
                    price: "565¥"
                    p_name: "Cracker Fita"

                ProductCard:
                    prd_id: "pudding"
                    image: "products/pudding.png"
                    price: "795¥"
                    p_name: "Lychee Pudding"
```
The cards contained in the scroll view are another class, which is ProductCards and it's a subclass of MDCard, as shown below:
```.kv
<ProductCard@MDCard>:
    image: ""
    p_name: ""
    price: ""
    prd_id: ""
    padding: 10
    orientation: "vertical"
    size_hint_x: .5
    on_release: app.root.get_screen("HomeScreen").goto_product(root.image,root.p_name,root.price, root.prd_id)
    size_hint_y: None
    height: 240
    md_bg_color: "#f8e2ca"

    canvas.before:
        Color:
            rgba: (0.414, 0.340, 0.313, 1)  #rgba of #6a5750 (i'm rly glad i made the chrome extension)
        Line:
            width: 3
            rounded_rectangle: (self.x, self.y, self.width, self.height, 30)

    

    BoxLayout:
        orientation: "vertical"
        size_hint_y: 0.55
        Image:
            source: root.image
            size_hint_y: 1
    BoxLayout:
        size_hint_y: 0.1
    BoxLayout:
        orientation: "vertical"
        size_hint_y: 0.35
        padding: 5
        spacing: 2

        MDLabel:
            text_color: "#6a5750"
            font_name: "Lora.ttf"
            text: root.p_name
            font_size: "14sp"
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text_color: "#6a5750"
            text: root.price
            font_size: "10sp"
            size_hint_y: None
            height: self.texture_size[1]
```
Having this simplifies the code for creating a new product on the scrollView in the home page. 


### Success criteria 4 & 5: cart functions ad confirmation
On the product detail page, there's the button "add to your cart" which allows the user to add a product to their cart by adding the product as an entry into the cart_orders table through SQLite. After that, a pop up would appear to confirm the item is added into the cart. 
```.py
def add_to_cart(self):
        if not self.dialog:
            self.dialog = MDDialog(
                md_bg_color= "f8e2ca",
                title="[color=#6a5750]Thank you![/color]",
                text="[color=#6a5750]Item successfully added to your cart!\n\nRedirecting you back to the home page now. Enjoy your shopping![/color]",
                buttons=[
                    MDRaisedButton(
                        text="[color=f8e2ca]Close[/color]",
                        on_release=self.redirect_to_home
                    )
                ],
            )
        db1 = sqlite3.connect("login.sql")
        c = db1.cursor()
        insert_query = "INSERT INTO cart_orders (name, price, username) VALUES (?,?,?)"
        c.execute(insert_query, (self.p_name, self.p_price, str(LoginScreen.current_user)))
        db1.commit()
        c.close()
        self.dialog.open()

    def redirect_to_home(self, *args):
        self.dialog.dismiss()
        self.parent.current = "HomeScreen"
```
After that, when going into the cart screen (CartScreen), items in the order are loaded using the load_cart_items() function, which selects all the products which has the attribute username with the value of the username of the current user. The names and prices are the information shown on the scroll view of list items. 
```.py
 def load_cart_items(self):
        self.ids.cart_items.clear_widgets()

        self.total = 0

        conn = sqlite3.connect("login.sql")
        cursor = conn.cursor()
        cursor.execute(f"SELECT name, price FROM cart_orders where username = '{LoginScreen.current_user}'")
        rows = cursor.fetchall()
        conn.close()

        for name, price in rows:
            self.total += price
            self.add_cart_item(name, price)

        self.update_total_price(self.total)
```


---
Coded using the language Python. 
Chatgpt has been used for debugging purposes in this project. (https://chatgpt.com/)

Product information and image credits to https://www.pinoys.eu/, specifically:
- https://www.pinoys.eu/tl/p/instant-pho-bo-rice-noodle-soup-beef-flavour-60-g-vifon#
- https://www.pinoys.eu/tl/p/crispy-onions-in-chili-oil-210-g-lao-gan-ma#
- https://www.pinoys.eu/tl/p/shin-ramyun-spicy-120-g-nongshim#
- https://www.pinoys.eu/tl/p/cracker-fita-300-g-m-y-san
- https://www.pinoys.eu/tl/p/fruit-pudding-lychee-flavour-480-g-cocon#
- https://www.pinoys.eu/tl/p/shougong-taiwanese-style-cake-120-g-ranli
- https://www.pinoys.eu/tl/p/mochi-peanut-rice-cake-210-g-szu-shen-po
- https://www.pinoys.eu/tl/p/rice-cake-sticks-600-g-matamun

(images processed by Ann Tsai using Microsoft Photos application and https://www.remove.bg/)

## Criterion D: Functionality


## Appendix
![image](https://github.com/user-attachments/assets/afb1ad85-ddfc-4e63-8efe-75b9ac3f4201)

Screenshot of the transcript of the interview with the client. Document could be accessed here: https://docs.google.com/document/d/13I5UP34eFG2Ku2RaJQjZK8SNfTHSezlCicRTwNSn8mU/edit?tab=t.0


[^1]: “3.9.13 Documentation.” Docs.python.org, 2001, docs.python.org/3.9/. Accessed 11 Mar. 2025.

[^2]: “Benefits of SQLite as a File Format.” Www.sqlite.org, www.sqlite.org/aff_short.html. Accessed 12 Mar. 2025.

[^3]: GeeksforGeeks. “Python Language Advantages and Applications - GeeksforGeeks.” GeeksforGeeks, 23 Oct. 2017, www.geeksforgeeks.org/python-language-advantages-applications/. Accessed 12 Mar. 2025.

[^4]: HusamFathi. “Kivy and KivyMD Online Shop UI Speed Code.” YouTube, 10 July 2021, youtu.be/ADfGpvObM4g?si=J_I0bXjlCy_2kGVR. Accessed 2 Mar. 2025.

[^5]: Rodrígue, Andrés, et al. “KivyMD 1.1.1 Documentation.” Kivymd.readthedocs.io, 2022, kivymd.readthedocs.io/en/1.1.1/. Accessed 11 Mar. 2025.

[^6]: SB Developer. “How to Create Login Form with Splash Screen Using KivyMD | Durar Portal LLC | Login Page.” YouTube, 24 July 2021, youtu.be/f2VVEcN4CU4?si=DHQjInZ6GuFCMtrL. Accessed 27 Feb. 2025.

[^7]: “Why Use a Database? - Information Handling Software - GCSE ICT Revision - WJEC.” BBC Bitesize, www.bbc.co.uk/bitesize/guides/znvyt39/revision/4. Accessed 12 Mar. 2025.
