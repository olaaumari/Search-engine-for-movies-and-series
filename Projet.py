#Partie 2
import pandas as pd
import os
path=os.getcwd()
print(path)

def importation_fichiers():

    print("Veuillez entrer le nom de fichier amazon :")
    global amazon
    amazon=pd.read_csv(path+"\\"+input(), sep=",")
    
    print("Veuillez entrer le nom de fichier netflix :")
    global netflix
    netflix=pd.read_csv(path+"\\"+input(), sep=",")
    
    print("Veuillez entrer le nom de fichier disney :")
    global disney
    disney=pd.read_csv(path+"\\"+input(), sep=",")
    
    print("Veuillez entrer le nom de fichier IMDB:")
    global IMDB
    IMDB=pd.read_csv(path+"\\"+input(), sep=",")
    
    
#QUESTION 1


def question1_part2():
    Recherche = str(input("Recherche (Entrez le titre de film/série que vous cherchez):")).title()
    titreA = amazon["title"].tolist()
    titreD = disney["title"].tolist()
    titreN = netflix["title"].tolist()
    if Recherche in titreA:
        print(Recherche+ ' est disponible sur la plateforme Amazon prime')
    elif Recherche not in titreA:
        titreA = amazon[amazon['title'].str.contains(Recherche)].loc[:,'title'].tolist()
        print(Recherche + " n'est pas disponible sur Amazon prime video, voici des suggestions : ", titreA[:5])  
    else:
        print(Recherche + " n'est pas disponible sur la plateforme Amazon prime")
    if Recherche in titreD:
        print(Recherche +' est disponible sur la plateforme Disney plus')
    elif Recherche not in titreD:
        titreD = disney[disney['title'].str.contains(Recherche)].loc[:,'title'].tolist()
        print(Recherche + " n'est pas disponible sur Disney plus voici des suggestions : ", titreD[:5])
    else:
        print(Recherche +" n'est pas disponible sur la plateforme Disney plus")  
    if Recherche in titreN:
        print(Recherche +" est disponible sur la plateforme Netflix")
    elif Recherche not in titreN:
        titreN = netflix[netflix['title'].str.contains(Recherche)].loc[:,'title'].tolist()
        print(Recherche + " n'est pas disponible sur Netflix, voici des suggestions : ", titreN[:5])      
    else:
        print(Recherche + " n'est pas disponible sur la plateforme Netflix ")
        
    releaseA = amazon[amazon['title'].str.contains(Recherche)].loc[:,'release_year'].tolist()
    descriptionA = amazon[amazon['title'].str.contains(Recherche)].loc[:,'description'].tolist()
    acteurA = amazon[amazon['title'].str.contains(Recherche)].loc[:,'cast'].tolist()
    genreA = amazon[amazon['title'].str.contains(Recherche)].loc[:,'listed_in'].tolist()

    releaseD = disney[disney['title'].str.contains(Recherche)].loc[:,'release_year'].tolist()
    descriptionD = disney[disney['title'].str.contains(Recherche)].loc[:,'description'].tolist()
    acteurD = disney[disney['title'].str.contains(Recherche)].loc[:,'cast'].tolist()
    genreD = disney[disney['title'].str.contains(Recherche)].loc[:,'listed_in'].tolist()


    releaseN = netflix[netflix['title'].str.contains(Recherche)].loc[:,'release_year'].tolist()
    descriptionN = netflix[netflix['title'].str.contains(Recherche)].loc[:,'description'].tolist()
    acteurN = netflix[netflix['title'].str.contains(Recherche)].loc[:,'cast'].tolist()
    genreN = netflix[netflix['title'].str.contains(Recherche)].loc[:,'listed_in'].tolist()

    note = IMDB[IMDB['title'].str.contains(Recherche)].loc[:,'avg_vote'].tolist()


    if Recherche in titreA:
        
        print(Recherche+ ' est sortie en',  releaseA[0])
        print("Voici le synopsis de ce programme : ", descriptionA[0])
        print("Les acteurs principaux sont" , acteurA[0])
        print("Genre : " , genreA[0])
        note = IMDB[IMDB['title'].str.contains(Recherche)].loc[:,'avg_vote'].tolist()
        print("la note donnée en moyenne par les utilisateurs du site est :", note[0])

    if Recherche in titreD:
        print(Recherche+ ' est sortie en',  releaseD[0])
        print("Voici le synopsis de ce programme : ", descriptionD[0])
        print("Les acteurs principaux sont" , acteurD[0])
        print("Genre : " , genreD[0])
        note = IMDB[IMDB['title'].str.contains(Recherche)].loc[:,'avg_vote'].tolist()
        print("la note donnée en moyenne par les utilisateurs du site est :", note[0])

    if Recherche in titreN:
        print(Recherche+ ' est sortie en',  releaseN[0])
        print("Voici le synopsis de ce programme : ", descriptionN[0])
        print("Les acteurs principaux sont" , acteurN[0])
        print("Genre : " , genreN[0])
        note = IMDB[IMDB['title'].str.contains(Recherche)].loc[:,'avg_vote'].tolist()
        print("la note donnée en moyenne par les utilisateurs du site est : ", note[0])
    return
    
#QUESTION2

def question2_part2():

    Recherche= str(input("Veuillez entrez le nom d'un acteur:")).title()
    net = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'cast'].tolist()
    ama = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'cast'].tolist()
    dis = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'cast'].tolist()

    if len(net) > (len(dis) or len(ama)):
        net = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'cast'].tolist()
        filmserienet = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'title'].tolist()
        print(Recherche+ ' a joué dans' , len(net) , 'films ou séries sur Netflix')
        print('Voici ces films ou série' , filmserienet[:10])
    elif len(ama) > (len(dis) or len(net)):
        ama = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'cast'].tolist()
        filmserieama = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'title'].tolist()
        print(Recherche+ ' a joué dans' , len(ama) , 'films ou séries sur Amazon prime video')
        print('Voici ces films ou série' , filmserieama[:10])
    else:
        dis = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'cast'].tolist()
        filmseriedis = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'title'].tolist()
        print(Recherche+ ' a joué dans' , len(dis), 'films ou séries sur Disney plus')
        print('Voici ces films ou série' ,filmseriedis[:10])



    releaseAa = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'release_year'].tolist()
    descriptionAa = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'description'].tolist()
    genreAa = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'listed_in'].tolist()
    typeAa = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'type'].tolist()
    ClassificationAa = amazon[amazon['cast'].str.contains(Recherche, na=False)].loc[:,'rating'].tolist()



    releaseDa = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'release_year'].tolist()
    descriptionDa = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'description'].tolist()
    genreDa = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'listed_in'].tolist()
    typeDa = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'type'].tolist()
    ClassificationDa = disney[disney['cast'].str.contains(Recherche, na=False)].loc[:,'rating'].tolist()



    releaseNa = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'release_year'].tolist()
    descriptionNa = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'description'].tolist()
    genreNa = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'listed_in'].tolist()
    typeNa = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'type'].tolist()
    ClassificationNa = netflix[netflix['cast'].str.contains(Recherche, na=False)].loc[:,'rating'].tolist()







    if len(net) > (len(dis) or len(ama)):

        print("Voici le synopsis des programmes où a joué " + Recherche +" :", descriptionNa[:5])
        print("Dans l'ordre ils sont sortie en ",  releaseNa)
        print("Genre de ces films ou série dans l'ordre : : " , genreAa[:10])
        print("Ainsi que leurs types dans l'ordre : " , typeNa)
        print("Classification : " , ClassificationNa)


    elif len(ama) > (len(dis) or len(net)):
        print("Dans l'ordre ils sont sortie en ",  releaseAa)
        print("Voici le synopsis des programmes où a joué " + Recherche +" :", descriptionDa[0])
        print("Genre de ces films ou série dans l'ordre :  : " , genreAa[:10])
        print("Ainsi que leurs types dans l'ordre : " , typeAa)
        print("Classification : " , ClassificationAa)    

    else:
        print("Dans l'ordre ils sont sortie en ",  releaseDa)
        print("Voici le synopsis des programmes où a joué " + Recherche +" :", descriptionDa[:10])

        print("Genre de ces films ou série dans l'ordre : " , genreDa[:10])
        print("Ainsi que leurs types dans l'ordre : " , typeDa)
        print("Classification : " , ClassificationDa)
    return

    
#QUESTION3



def question3_part2():
    
    typeducontenu = str(input("Veuillez saisir un type du contenu (Movie/TV Show):"))
    genre = str(input("Veuillez entrez un genre de film/série:")).title()

    amafs = amazon[(amazon['type'].str.contains(typeducontenu)) &           (amazon['listed_in'].str.contains(genre))].sort_values('release_year',ascending = False)
    print(len(amafs) ," résultats correspondant à vos critères de recherche", "Sur la plateforme Amazon")
    print("Voici les trois programmes les plus récents "  ,amafs.iloc[:3, 2].tolist())

    disfs = disney[(disney['type'].str.contains(typeducontenu)) & (disney['listed_in'].str.contains(genre))].sort_values('release_year',ascending = False)
    print(len(disfs)," résultats correspondant à vos critères de recherche", "Sur la plateforme disney")
    print("Voici les trois programmes les plus récents "  ,disfs.iloc[:3, 2].tolist())

    netfs = netflix[(netflix['type'].str.contains(typeducontenu)) & (netflix['listed_in'].str.contains(genre))].sort_values('release_year',ascending = False)
    print(len(netfs)," résultats correspondant à vos critères de recherche", "Sur la plateforme netflix")
    print("Voici les trois programmes les plus récents"  ,netfs.iloc[:3, 2].tolist())
    return
#Question4




#Question4

def question4_part2():

        préférences = str(input("Veuillez entrez votre votre préference (Movie/TV Show):"))
        genre = str(input("Veuillez entrez un genre de film:")).title()
        rating = str(input("Veuillez entrez une classification du contenu:")).title()
        country = str(input("Veuillez entrez un pays de producteur de film/série ")).title()
        cast = str(input("veuillez entrez le nom d'un acteur:")).title()

        ama4 = amazon[(amazon['type'].str.contains(préférences)) & (amazon['listed_in'].str.contains(genre)) & (amazon['rating'].str.contains(rating)) & (amazon['country'].str.contains(country)) & (amazon['cast'].str.contains(cast))].sort_values('release_year',ascending = False)
        ama4a = amazon[(amazon['type'].str.contains(préférences)) & (amazon['listed_in'].str.contains(genre)) & (amazon['rating'].str.contains(rating)) & (amazon['country'].str.contains(country)) & (amazon['cast'].str.contains(cast))].sort_values('date_added',ascending = False)

        print("Suggestion pour Amazon Prime video selon l'année de sortie du film ou de la série :")
        print(ama4.iloc[:5, 2].tolist())
        print("Suggestion pour Amazon Prime video selon la date d’ajout sur la plateforme  :")
        print(ama4a.iloc[:5, 2].tolist())


        dis4 = disney[(disney['type'].str.contains(préférences)) & (disney['listed_in'].str.contains(genre)) & (disney['rating'].str.contains(rating)) & (disney['country'].str.contains(country)) & (disney['cast'].str.contains(cast))].sort_values('release_year',ascending = False)
        dis4a = disney[(disney['type'].str.contains(préférences)) & (disney['listed_in'].str.contains(genre)) & (disney['rating'].str.contains(rating)) & (disney['country'].str.contains(country)) & (disney['cast'].str.contains(cast))].sort_values('date_added',ascending = False)

        print("Suggestion pour Disney plus selon l'année de sortie du film ou de la série : ")
        print(dis4.iloc[:5, 2].tolist())
        print("Suggestion pour Disney plus selon la date d’ajout sur la plateforme  :")
        print(dis4a.iloc[:5, 2].tolist())



        net4 = netflix[(netflix['type'].str.contains(préférences)) & (netflix['listed_in'].str.contains(genre)) & (netflix['rating'].str.contains(rating)) & (netflix['country'].str.contains(country)) & (netflix['cast'].str.contains(cast))].sort_values('release_year',ascending = False)
        net4a = netflix[(netflix['type'].str.contains(préférences)) & (netflix['listed_in'].str.contains(genre)) & (netflix['rating'].str.contains(rating)) & (netflix['country'].str.contains(country)) & (netflix['cast'].str.contains(cast))].sort_values('date_added',ascending = False)

        print("Suggestion pour netflix selon l'année de sortie du film ou de la série : ")
        print(net4.iloc[:5, 2].tolist())
        print("Suggestion pour Netflix selon la date d’ajout sur la plateforme  :")
        print(net4a.iloc[:5, 2].tolist())
        return


if __name__ == '__main__':
    importation_fichiers()
    question1_part2()
    question2_part2()
    question3_part2()