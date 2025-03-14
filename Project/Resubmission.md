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
I have chosen to use Python to create a GUI with kivymd and SQLite due to many reasons. Python is a high-level, interpreted programming language known for its simplicity, readability, and easiness to use. One of Python's strongest features is it's third-party libraries[^3] and frameworks. For this project, I selected kivymd as it is very similar to Google’s Material Design spec as the goal of this framework is to be the easier to use version of Google's Material Design[^5]. Because of the choice of using kivymd, there are a lot of built in widgets and elements that aesthetically pleasing. Moreover, kivymd could potentially be ran on an Android or iOS platform, creating flexibility for future deployments. 

Furthermore, using a database in an application like this would bring much benefits. It is very easy and fast to find specfic information using the query, and data can be imported into other applications if a database is used. [^7] In this project,Python is combined with SQLite in this project due to their compatibility. SQLite is a lightweight, serverless, and self-contained database engine, which makes it suitable for local data storage as they take up little space[^2].

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




**What I changed:** I removed the testing data from the database screenshot in this section. 
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




![image](https://github.com/user-attachments/assets/bd8585a7-c0ce-4053-a884-2e2e55f4b1da)

**Fig.8** table "user" in login.sql in the database





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



**What I changed:** I corrected the format by adding the column "task number" and added words that match the criteria in the planned action column. 

### Record of Tasks
| **Task number** | **Planned action**                                                | **Planned outcome**                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Time estimate** | **Target completion date** | **Criteria** |
|-----------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------|--------------|
| 1               | Planning: Interview the client for a description of the problem   | After listening to the client's description of the problem, I would finish writing the problem definition                                                                                                                                                                                                                                                                                                                                                                                 | 30 min            | Feb 4                      | A            |
| 2               | Planning: Meet with the client again to show the success criteria | After writing the definition of the problem, I would highlight the main issues and create success criterion based on them and check with the client                                                                                                                                                                                                                                                                                                                                       | 35 min            | Feb 7                      | A            |
| 3               | Planning: Research and propose a solution                         | Research methods and write a proposed solution based on the finalized success criteria and justify choice of tools and methods with citations                                                                                                                                                                                                                                                                                                                                             | 1 hr              | Feb 11                     | A            |
| 4               | Design: Create design plan                                        | 1. Create a color scheme using Coolors and the logo for the application using Canva. <br>2. Find and download from Google fonts the font that is going to be used in the application. <br>3. Find and record the information of the example products sold on the application and note down their links for citation. <br>4. Download all images needed, process them as needed, and move them to this project's folder. <br>5. Note down relevent design information on a Google Document | 1 hr 30 min       | Feb 19                     | B            |
| 5               | Design: Create diagrams for backend of the application            | Create a UML diagram, ER diagram, 3 flow diagrams - one simple, one medium, one hard, and a system diagram                                                                                                                                                                                                                                                                                                                                                                                | 3 hrs             | Feb 26                     | B            |
| 6               | Design: Create a test plan                                        | Create a test plan table that provides instructions on input and expected output of the application matching the success criteria                                                                                                                                                                                                                                                                                                                                                         | 1 hr              | Feb 28                     | B            |
| 7               | Development: Create the log in page user interface (UI)           | Code, using kivymd and some Python on Pycharm, the log in UI. It follows the design plan (color scheme, font, logo)                                                                                                                                                                                                                                                                                                                                                                       | 40 min            | Mar 1                      | C            |
| 8               | Development: Create the sign up page UI                           | Code, using kivymd and some Python on Pycharm, the sign up UI by modifying the log in UI. It follows the design plan (color scheme, font, logo)                                                                                                                                                                                                                                                                                                                                           | 20 min            | Mar 1                      | C            |
| 9               | Development: Create the home page UI                              | Code, using kivymd and some Python on Pycharm, the home page UI that has a scrollable display of products and a navigation bar at the bottom. It follows the design plan (color scheme, font, logo, product information and price)                                                                                                                                                                                                                                                        | 1 hr              | Mar 1                      | C            |
| 10              | Development: Create the product details page UI                   | Code, using kivymd and some Python on Pycharm, the product page UI. It follows the design plan (color scheme, font, product information and price)                                                                                                                                                                                                                                                                                                                                        | 1 hr              | Mar 2                      | C            |
| 11              | Development: Create the profile page UI                           | Code, using kivymd and some Python on Pycharm, the profile page UI. It follows the design plan (color scheme, font, logo)                                                                                                                                                                                                                                                                                                                                                                 | 45 min            | Mar 2                      | C            |
| 12              | Development: Develop the log in and sign up system                | Code, using a database (SQLite) and Python on Pycharm, the functions of the log in and sign up system using the test plan as a reference to test it's functionality                                                                                                                                                                                                                                                                                                                       | 1 hr 30 min       | Mar 5                      | C            |
| 13              | Development: Populate the products table                          | Using the SQLite console, populate the products table (already created in the Python code) with the relevent product information                                                                                                                                                                                                                                                                                                                                                          | 1 hr              | Mar 6                      | C            |
| 14              | Development: Develop the product details system                   | Code, using Python on Pycharm, the functions of automatically updating the information of the products in the UI based on the contents in a table                                                                                                                                                                                                                                                                                                                                         | 1 hr 30 min       | Mar 7                      | C            |
| 15              | Development: Create the cart page UI                              | Code, using kivymd and some Python on Pycharm, the cart page UI. It follows the design plan (color scheme, font, logo, product information and price).                                                                                                                                                                                                                                                                                                                                    | 1 hr              | Mar 8                      | C            |
| 16              | Development: Develop the cart system                              | Code, using Python on Pycharm, the functions of adding items to the cart and showing items on the cart page UI based on the contents in a table for orders, showing the total after adding up the price, and clearing the table after user completes order                                                                                                                                                                                                                                | 1 hr              | Mar 8                      | C            |
| 17              | Development: Develop the delivery time popup system               | Code, using Python and some kivymd on Pycharm, the functions of randomizing the delivery time and showing it on a popup after order is confirmed. It follows the design plan (color scheme, font)                                                                                                                                                                                                                                                                                         | 1 hr              | Mar 8                      | C            |
| 18              | Development: Debug and test run                                   | Run the application then test it using the instructions on the test plan table. Adjust the application as needed.                                                                                                                                                                                                                                                                                                                                                                         | 30 min            | Mar 9                      | C            |
| 19              | Design: Refine test plan                                          | Refine the test plan after finishing the whole application and testing it out using the test plan, removing redundant parts and make the instructions more detailed and tailored to the application.                                                                                                                                                                                                                                                                                      | 30 min            | Mar 9                      | B            |
| 20              | Development: Identify tools and techniques used                   | Identify the tools (packages and libraries) used and techniques used, list them out on the .md file.                                                                                                                                                                                                                                                                                                                                                                                      | 30 min            | Mar 9                      | C            |
| 21              | Development: Review the code and explain it                       | Write down what each snippet of code does and explain it on the .md file                                                                                                                                                                                                                                                                                                                                                                                                                  | 3 hrs             | Mar 9                      | C            |
| 22              | Functionality: Record the demonstration video                     | Record the demonstration video and in it, test the application using the test plan.                                                                                                                                                                                                                                                                                                                                                                                                       | 30 min            | Mar 11                     | D            |
| 23              | Design: Finalize Record of Tasks table                            | Make sure everything is completed based on the record of tasks table                                                                                                                                                                                                                                                                                                                                                                                                                      | 30 min            | Mar 12                     | B            |




**What I changed:** I changed this section to be in first person. I removed the redundant parts. However, I didn't have enough time to finish talking about everything I want to. 
## Criterion C: Development

### Techniques used
- **Object-Oriented Programming (OOP)**: I used classes to structure the application, for example, the different screens (HomeScreen, CartScreen, etc.) in this application, and the product cards.
- **Front end/User Interface (UI) programming**: I used kivymd to develop the front end of this application which allows the user to interact with this application. For example, the buttons that allow user to log-in, sign-up and add items to their carts. 
- **Hashing**: I used this to store password securely in a database by encrypting it. 
- **Interacting with Databases**: I used SQLite to interact with databses, and this allows data to be saved and retrieved when required. Used to store user information, product information, etc.

### Packages used
- SQLite3
- kivy
- kivymd [^5]
- passlib
- random

### User Interface Programming
I didn't really know how to approach UI design using kivymd at first, because it has so many elements that I didn't know. I was struggling to create a scrollable page, and also mainly positioning things properly on a Screen class object. Hence, I decided to follow tutorials and learn as I observe how others do it. For the log-in and sign up page, I followed a tutorial[^6] for some parts of the layout, but added my personal fonts and color, and adjusted quite a lot of things to fit the theme I am going for. I followed another tutorial[^4] for the home page too, to figure out how scrollable view of cards could be achieved, and how a navigation bar could be made, but I also adjusted it a lot to fit my theme. After watching it, I finally understood how scroll layouts work, and also I finally understand fully how to use ```pos_hint```. Below is an example:
```.py
MDBoxLayout:
        padding: 30
        spacing: 10
        orientation: "vertical"
        md_bg_color: "#e2c8ad"
        MDBoxLayout:
            size_hint_y: 0.3
            md_bg_color: "#e2c8ad"
            AnchorLayout:
                anchor_y: "top"
                anchor_x: "center"
                FitImage:
                    source: "logo-clear.png"
                    size_hint_y: 0.9
                    size_hint_x: 0.8
```
This code keeps the logo at the top using MDBoxLayout

```.py
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
```
This code creates a scrollable view that contains other objects. 

### Object Oriented Programming
At first, I created 8 separate product detail pages (one for each product). However, I wanted my code to be more dynamic because I had too much code which made it hard to debug and when I wanted to make changes, I had to change every one of them from the 8. Hence, I decided to use OOP becuase I was reminded that I could create classes. Below is an example of how I used classes to update product details and create only one product detail page. 

```.py
class ProductDetail(Screen):
    image = StringProperty("")
    p_name = StringProperty("")
    price = StringProperty("")
    prd_id = StringProperty("")
    p_price = 0
    dialog = None

    def update_info(self):
        # here's the arughgijerfiefl main problem

        query = f"SELECT * FROM products WHERE prd_id = '{self.prd_id}'"
        db = DatabaseManager(name="login.sql")
        result = db.search(query)
        # print(f"({self.prd_id}), {result}") #DEBUGGGGG :P
        db.close()

        if result and len(result) > 0:
            ingredients_text = result[0][3]
            allergens_text = result[0][4]
            restrictions_text = result[0][5]
            country_text = result[0][8]
            self.p_price = int(result[0][6])

            self.ids.ingredients.text = f"Ingredients: {ingredients_text}"
            self.ids.allergens.text = f"Allergens: {allergens_text}"
            self.ids.restrictions.text = f"Restrictions: {restrictions_text}"
            self.ids.country.text = f"Country of Origin: {country_text}"

    def on_pre_enter(self):
        self.update_info()
```

```.kv
ProductCardDeactivated:
                size_hint: None, None
                size: 560, 300
                image: root.image
                p_name: root.p_name
                price: root.price
                prd_id: root.prd_id
```

---
Coded using the language Python. [^1]
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
Video too big to upload directly to markdown file, so here's the google drive link: https://drive.google.com/file/d/1Qq90mxiF-FJBliXu_HrL3q5i114_p1IT/view?usp=sharing

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
