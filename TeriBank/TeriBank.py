from tkinter import *

fenetre = Tk()

largeur_ecran = 1920
hauteur_ecran = 1080


def login_screen():
    cadre_fond_accueil.delete(fenetre_bouton)

    cadre_login = Frame(cadre_fond_accueil, bg=None, height=180, width=230)
    username = Label(cadre_login, text="Nom d'utilisateur")
    password = Label(cadre_login, text="Mot de passe")
    new_customer = Button(cadre_login, text="Nouveau client?", fg='#0038c4', activeforeground="#69cbff",
                          overrelief='flat', command=new_customer_screen)

    u_n = Entry(cadre_login)
    p_w = Entry(cadre_login, show='*')
    bouton_valider = Button(cadre_login, text="Valider", command=quit)
    username.pack()
    u_n.pack()
    password.pack()
    p_w.pack()
    bouton_valider.pack()
    new_customer.pack()

    fenetre_login = cadre_fond_accueil.create_window(largeur_ecran / 2, (hauteur_ecran / 2) - 100, height=140,
                                                     width=230,
                                                     window=cadre_login)


def new_customer_screen():
    Ecran1.forget()
    cadre_banker_bg.create_image(largeur_ecran / 2, (hauteur_ecran / 2) - 100, image=banker_bg)
    cadre_formulaire = Frame(cadre_banker_bg, highlightthickness=3, )
    cadre_info_formulaire = Frame(cadre_formulaire)
    titre_formulaire = Label(cadre_formulaire, font=('Times New Roman', "35", 'normal'),
                             text="Formulaire d'inscription")
    nom = Label(cadre_info_formulaire, text='Nom:')
    prenom = Label(cadre_info_formulaire, text='Prenom:')
    nom_saisi = Entry(cadre_info_formulaire)
    prenom_saisi = Entry(cadre_info_formulaire)
    metier = Label(cadre_info_formulaire, text="Métier:")
    metier_saisi = Entry(cadre_info_formulaire)
    revenu_m = Label(cadre_info_formulaire, text="Revenu mensuel:")
    revenu_m_saisi = Entry(cadre_info_formulaire)
    id_user = Label(cadre_info_formulaire, text="Nom d'utilisateur:")
    id_saisi = Entry(cadre_info_formulaire)
    password = Label(cadre_info_formulaire, text="Mot de passe:")
    password_saisi = Entry(cadre_info_formulaire)

    register_button = Button(cadre_formulaire, text="Enregistrer", command=quit)

    fenetre_cadre_formulaire = cadre_banker_bg.create_window(largeur_ecran / 2, (hauteur_ecran / 2) - 100, width=700,
                                                             height=800, window=cadre_formulaire)
    cadre_banker_bg.pack(expand=YES)
    titre_formulaire.pack(side=TOP)
    cadre_info_formulaire.pack(expand=YES)
    nom.grid(column=0, row=0)
    prenom.grid(column=0, row=1)
    metier.grid(column=0, row=2)
    revenu_m.grid(column=0, row=3)
    id_user.grid(column=0, row=4)
    password.grid(column=0, row=5)

    nom_saisi.grid(column=1, row=0)
    prenom_saisi.grid(column=1, row=1)
    metier_saisi.grid(column=1, row=2)
    revenu_m_saisi.grid(column=1, row=3)
    id_saisi.grid(column=1, row=4)
    password_saisi.grid(column=1, row=5)

    register_button.pack(anchor='s')

    Ecran2.pack()


fenetre.title('TeriBank')
fenetre.geometry("1920x1080")
# Création des écrans

Ecran1 = Frame(fenetre)
Ecran2 = Frame(fenetre)

# Création des images

fond_accueil = PhotoImage(file='TB_Project/Page_daccueil.png')
cadre_fond_accueil = Canvas(Ecran1, width=largeur_ecran, height=hauteur_ecran)
cadre_fond_accueil.create_image(largeur_ecran / 2, (hauteur_ecran / 2) - 100, image=fond_accueil)
banker_bg = PhotoImage(file='TB_Project/pexels_thirdman_5060556.png')
cadre_banker_bg = Canvas(Ecran2, width=largeur_ecran, height=hauteur_ecran)
transparent = PhotoImage(file='TB_Project/fond_transparent.png')

# Création des onglets
barre = Menu(Ecran1)
fenetre['menu'] = barre

sousMenuCompte = Menu(barre, tearoff=0)
sousMenuGerer = Menu(barre, tearoff=0)
sousMenuFenetre = Menu(barre, tearoff=0)

barre.add_cascade(label='Compte', menu=sousMenuCompte)
barre.add_cascade(label='Gérer', menu=sousMenuGerer)
barre.add_cascade(label='Fenêtre', menu=sousMenuFenetre)

sousMenuCompte.add_command(label="Nouveau compte", command=None)

# Création des boutons

bouton_accueil = Button(Ecran1, width=15, height=2, font=("Arial", 15), text='Commencer', command=login_screen)
fenetre_bouton = cadre_fond_accueil.create_window(largeur_ecran / 2, hauteur_ecran - (hauteur_ecran / 5), anchor='s',
                                                  window=bouton_accueil)

# Affichage des éléments

cadre_fond_accueil.pack(expand=YES)
Ecran1.pack()

fenetre.mainloop()
