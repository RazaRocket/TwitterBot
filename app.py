from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)  # Pour mettre en pause tde 3sec le loading de la page
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)

    # search for a hashtag and then pull up the tweet apres avoir lancer app.py
    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get(
            'https://twitter.com/search?q='+hashtag+'&src=typd')  # fetch another link avec un sujet de notre choix
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # pour scroll down automatiquement
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in
                     tweets]  # pour tweets on cherche ts les éléments pour avoir leur data permalink path
            # print(links)
            for link in links:  # to loop over all of these & to pen it up again each individual links
                bot.get("https://twitter.com" + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(15)
                except Exception as ex:
                    time.sleep(70)


# Creation d'une instance pour la Class Twitter Bot
# Dedans il faudra mettre le mail associé au compte + mdp NE PAS PUSH CA SUR GITHUB
ed = TwitterBot('yourmail@mail.com', 'yourpassword')

# Appel de la fonction login
ed.login()

# Apres avoir fait bot.get
ed.like_tweet('webdevelopment')

# Ouvrir le terminal et faire python app.py
# Un messag d'erreur sort, il faut f12 la page de co twitter et regarder le placeholder du mail
# Il faut soit changer le temps du sleep (+ ta co internet est rapide + le nbre est bas
# et ajouter une variable email dans la fonction login

# Pour lancer le programme on va dans le terminal > python app.py
