#import
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from mylib import *
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivymd.uix.list import TwoLineRightIconListItem, IconRightWidget

#set window size
Window.size = (350, 580)
def lock_size(instance, width, height):
    Window.size = (350, 580)
Window.bind(on_resize=lock_size)

#homescreen!
class HomeScreen(Screen):

    def goto_product(self, image, p_name, price,prd_id):
        product_screen = self.parent.get_screen("ProductDetail")
        product_screen.image = image
        product_screen.p_name = p_name
        product_screen.price = price
        product_screen.prd_id = prd_id
        self.parent.current = "ProductDetail"




class ProductCard(MDCard):
    pass

class ProductCardDeactivated(MDCard):
    pass



#product detalisssssss
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



class ProfileScreen(Screen):
    def on_pre_enter(self, *args):
        if LoginScreen.current_user:
            self.ids.username_label.text = f'Hello there, {LoginScreen.current_user}'


class CartScreen(Screen):
    cart_items = ObjectProperty(None)
    total_price = ObjectProperty(None)
    dialog = None
    total = 0

    def on_enter(self):
        self.load_cart_items()

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

    def add_cart_item(self, name, price):
        item = TwoLineRightIconListItem(
            text=name,
            secondary_text=f"¥{price}"
        )

        remove_btn = IconRightWidget(icon="trash-can")
        remove_btn.item_name = name
        remove_btn.price = price
        remove_btn.text_color = "#f8e2ca"
        remove_btn.parent_item = item
        remove_btn.bind(on_release=self.remove_item)

        item.add_widget(remove_btn)
        self.ids.cart_items.add_widget(item)

    def remove_item(self, button):
        item_name = button.item_name
        price = button.price
        item_card = button.parent_item

        db = sqlite3.connect("login.sql")
        c = db.cursor()
        c.execute("DELETE FROM cart_orders WHERE name=(?) and username=(?)", (item_name,LoginScreen.current_user))
        db.commit()
        db.close()

        self.ids.cart_items.remove_widget(item_card)
        self.total = int(self.ids.total_price.text.split("¥")[1]) - price
        self.update_total_price(self.total)

    def update_total_price(self, total):
        self.ids.total_price.text = f"Total: ¥{self.total}"

    def confirm(self):
        if self.total != 0:
            db = sqlite3.connect("login.sql")
            c = db.cursor()
            c.execute("DELETE FROM cart_orders WHERE price>0 and username=(?)", (LoginScreen.current_user,))
            db.commit()
            db.close()
            arrival_days = random_days()
            self.dialog = MDDialog(
                    md_bg_color="f8e2ca",
                    title="[color=#6a5750]Thank you![/color]",
                    text=f"[color=#6a5750]Your order has been confirmed. Please pay on the arrival of the item. Item will arrive in {arrival_days} days. \n\nRedirecting you back to the home page now. Enjoy your shopping![/color]",
                    buttons=[
                        MDRaisedButton(
                            text="[color=f8e2ca]Close[/color]",
                            on_release=self.go_home
                        )
                    ],
                )
        else:
            self.dialog = MDDialog(
                md_bg_color="f8e2ca",
                title="[color=#6a5750]Warning![/color]",
                text=f"[color=#6a5750]You haven't ordered anything. Go put some products in your cart then do this again. \n\n(I thought this was common sense... Guess not :/) \n\nRedirecting you to the home page, dummy.[/color]",
                buttons=[
                    MDRaisedButton(
                        text="[color=f8e2ca]Close[/color]",
                        on_release=self.go_home
                    )
                ],
            )
        self.dialog.open()

    def go_home(self, *args):

        self.total = 0
        self.dialog.dismiss()
        self.parent.current = "HomeScreen"


#loginscreen
class LoginScreen(Screen):
    def on_pre_enter(self):
        #need this here else error
        Clock.schedule_once(self.clear_login, 0.01)
    def clear_login(self,placeholder):
        #added the placeholder because when I don't, it keeps saying two parameters were passed into this function which only takes one. (I'm going to assume that schedule_once() does that by default)
        self.ids.password.text = ""
        self.ids.username.text = ""


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



class SignupScreen(Screen):
    def on_enter(self):
        self.ids.pw1.text = ""
        self.ids.pw2.text = ""
        self.ids.signup_name.text = ""
        self.ids.signup_email.text = ""

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


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.theme_style = "Light"
        query_table1 = """
        create table if not exists user(
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            email text unique not null,
            password VARCHAR(256)

        )
        """
        query_table2 = """
                create table if not exists products(
                    id INTEGER PRIMARY KEY,
                    img text NOT NULL,
                    name TEXT not null,
                    ingredients text not null,
                    allergies text not null,
                    restrictions text not null,
                    price integer not null, 
                    prd_id text not null
                )
                """

        query_table3 = """
                        create table if not exists cart_orders(
                            id INTEGER PRIMARY KEY,
                            name text NOT NULL,
                            price integer not null, 
                            username text not null
                        )
                        """



        x = DatabaseManager(name = "login.sql")
        x.run_save(query=query_table1)
        x.run_save(query=query_table2)
        x.run_save(query=query_table3)
        x.close()



t = MyApp()
t.run()