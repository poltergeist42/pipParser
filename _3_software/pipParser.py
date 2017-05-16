#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Infos
=====

   :Projet:             pipParser
   :Nom du fichier:     pipParser.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170516

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.6
    
####

Descriptif
==========

    :Projet:            Ce petit programme permet de créer le fichier 'requierement' à
                        partir de la commande 'pip3 freeze'. Ce fichier est utile pour
                        l’installation des paquet sous python.

                        Une première variante du fichier 'nettoyée' des numéros de versions
                        peut être généré.
                        
                        Une seconde version 'customisée' peut être généré pour n'avoir
                        que les paquet présent dans un dossier donné.

####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Matrice
   
####
   
"""

from __future__ import absolute_import
import os, sys
sys.path.insert(0,'..')         # ajouter le répertoire précédent au path (non définitif)
                                # pour pouvoir importer les modules et paquets parent
    
import argparse

class C_pipParser( object ) :
    """ Class permettant d'effectuer des traitemant sur le fichier 'requierments' générer
        par la commande 'pip freeze'
    """
    def __init__( self) :
        """ **__init__()**
        
            Création et initialisation des variables globales de cette Class
        """
        self._v_dir             = os.getcwd()
                                    # os.getcwd() : permet de récupérer le chemin
                                    # du répertoire local
        self._v_fileName        = 'myRequierment.txt'
        self._v_fileNameNoVers  = 'myRequierment_noVers.txt'
        self._v_customFile      = 'myRequierment_custom.txt'
        self._t_fullFileName    = os.path.join(self._v_dir, self._v_fileName)

####
        
    def __del__(self) :
        """ **__del__()**
        
            Permet de terminer proprement l'instance de la Class courante
        
            il faut utilise : ::
            
                del [nom_de_l'_instance]
                
            *N.B :* Si l'instance n'est plus utilisée, cette méthode est appelée 
            automatiquement.
        """
        ## Action
        v_className = self.__class__.__name__
        
####

    def f_setFilePath(self, v_localWorkDir=None) :
        """ Permet de définir le chemin dans lequel est créé le fichier. Ce chemin est
            utilisé comme répertoire de travail (workdir).
        """
        ## Action
        if v_localWorkDir :
            self._v_dir = os.path.normpath(v_localWorkDir)
            os.chdir(self._v_dir)
        else :
            print( "Aucun chemin n'a été spécifié. le chemin par défaut sera utilisé" /       " : \n {}".format(self._v_dir)
                 )
                
####
                
    def f_getFilePath(self) :
        """ Retourne le chemin dans lequel est créer le fichier.
        
            **N.B** : Ce chemin correspond au répertoire courant (workdir).
        """
        ## Action
        return self._v_dir
        
####

    def f_setFileName(self, v_fileName=None) :
        """ Permet de définir le nom du fichier.
            **N.B** : Le format attendu est de type 'str'
        """
        ## Action
        if not v_fileName :
            print( "Le nom du fichier sera : {0}\n" /
                   "Le nom du fichiers sans version sera : {1}\n" /
                   "Le nom du fichiers customisé sera : {2}".format(
                   self._v_fileName, self._v_fileNameNoVers, self._v_customFile
                   )
                 )
        else :
            self._v_fileName = "{}.txt".format(v_fileName)
            self._v_fileNameNoVers = "{}_noVers.txt".format(v_fileName)
            self._v_customFile = "{}_custom.txt".format(v_fileName)

####

    def f_getFileName(self) :
        """ Retourne le nom des fichiers sous la forme d'un tuple
        
            Ces nom sont sous la forme : ::
            
                *.txt           --> Fichier générer par pip
                *_noVers.txt    --> Fichier sans les numéros de version des paquets
                *_custom        --> Fichier personalisé
        """
        ## Action
        return (self._v_fileName, self._v_fileNameNoVers, self._v_customFile)
            
####

    def f_setFullFileName(self) :
        """ Permet définir les fichiers et leur chemin sous la forme d'un tuple 
            comportant deux string composées de cette façon : ::
        
                [chemin_du_fichier]\[nom_du_fichier]
        """
        ## Action
        t_fileName = f_getFileName()
        for i in t_fileName() :
            self._t_fullFileName.append( os.path.join(self._v_dir, i) )
                                    
####
            
    def f_getFullFileName(self) :
        """ Retourne le Nom des fichiers précédés de leur chemin (retourne un tuple).
        """
        ## Action
        return self._t_fullFileName

####

    def f_makeRequiermentFile(self, v_dirPath=None, v_fileName=None) :
        """ Permet de créer le fichier requierement de pip freeze. la commande qui va
            être exécutée sera : ::
            
                pip3 freeze > [nom_du_fichier]
                
            **v_dirPath** : Permet de définir le chemin dans lequel est créé le fichier.
            Ce chemin est utilisé comme répertoire de travail (workdir). Si il est définie, la méthode 'f_setFilePath()' sera appelée.
            
            **v_fileName** : Permet de définir le nom du fichier. Si il est définie, la
            méthode 'f_setFileName()' sera appelée.
            
            **N.B** : Le format attendu est de type 'str'
        
        """
        ## Action
        if v_dirPath :
            self.f_setFilePath(v_dirPath)
            
        if v_fileName :
            self.f_setFileName(v_fileName)
            
        self.f_setFullFileName()
        os.system( "pip3 freeze > {}".format(self.f_getFullFileName()[0]) )
        
####
        
    def f_makeNoVersFile( self ) :
        """ Permet de créer le ficher noVers à partir du fichier générer par pip
        """
        ## Action
        v_chaine = '='
        v_noVersFileToDel = self.f_getFullFileName()[1]

        with open( self.f_getFullFileName()[0], 'r') as versFile :
            for _, _, l_fichier in os.walk( self._v_dir ) :
                if v_noVersFileToDel in l_fichier :
                    os.remove( v_noVersFileToDel )
                    
            with open( self.f_getFullFileName()[1], 'a') as v_noVersFile :
                for v_line in versFile : 
                    if not v_chaine in v_line :
                        v_noVersFile.write( v_line )
                    else :
                        if v_chaine in v_line :
                            for i in range( len(v_line) ) :
                                if v_line[i] == v_chaine :
                                    v_newLine = "{}\n".format(v_line[:i])
                                    if v_newLine[-2] == v_chaine :
                                        pass
                                    else :
                                        v_noVersFile.write( v_newLine )
                                    
####
                                    
    def f_makeCustomFile( self ) :
        """ Permet de créer le fichier 'requierment' en parcourant le dossier '_v_dir'.
            Tous les fichiers portant l’extension '.whl' seront ajoutés au fichier
            '_v_customFile'
        """
        ## Action
        v_customFileToDel = self.f_getFullFileName()[2]
        for _, _, l_fichier in os.walk( self._v_dir ) :
            if v_customFileToDel in l_fichier :
                os.remove( v_customFileToDel )
                
        with open( self.f_getFullFileName()[2], 'a') as v_customFile :
            for _, _, l_file in os.walk( self._v_dir ) :
                for i in range( len(l_file) ) :
                    if l_file[i][-4:] == ".whl" :
                        v_customFile.write( "{}\n".format(l_file[i]) )
        
    
####                                    

def main() :
    """ Fonction principale

        :arg makefile:      -m ou --makefile. Permet de passer en mode création de
                            fichier.
                            
                            Le premier fichier est le fichier générer par la commande : :: 
                                
                                pip3 freeze > nom_du_fichier. 
                            
                            Ce fichier sera au minimum l'unique fichier générer.
                            
        :arg filename:      -f ou --filename. Permet de spécifier le nom du fichier.
                            Ce nom doit être spécifier sans l'extension car
                            l'extension '.txt' sera automatiquement ajoutée.
                            
                            Si aucun nom n'est renseigné , le nom du fichier par défaut
                            sera : 'myRequierment.txt'
                            
        :arg pathfile:      -p ou --pathfile. Permet de spécifier le chemin d'accès
                            des fichiers.
                            
                            Si aucun chemin n'est renseigné, le chemin par défaut sera
                            le répertoire courant( '.' ).
                            
        :arg askinfo:       -a ou --askinfo. Lance une invite de commande pour remplir
                            le nom du fichier et son chemin d'accès.
                            
                            Si l'un des arguments 'filename' ou 'pathfile' et passé en
                            même temps que 'askinfo', ils seront ignoré.
                            
                            Si aucun nom ou chemin n'est renseigné dans l'invite de
                            commande, le nom du fichier par défaut sera :
                            'myRequierment.txt' et le chemin par défaut sera le répertoire
                            courrant( '.' ).
                            
        :arg novers:        --novers. Si cet attribut est ajouté, un fichier
                            supplémentaire sera généré. Ce fichier est une copie du
                            premier nettoyer des numéros de versions qui accompagne
                            normalement chaque noms présent dans le fichiers généré par
                            'pip'. Ce fichier sera nommé de la même façon que
                            le premier avec le suffixe '_noVers' en plus.
                            
        :arg custom:        --custom. Si cet attribut est ajouté, un fichier
                            'requierement' sera créer en parcourant le chemin dossier
                            donné dans 'pathfile'. Tous les fichiers portant l’extension
                            '.whl' seront ajoutés au fichier. Ce fichier sera nommé de la
                            même façon que le premier avec le suffixe '_custom' en plus.
    """
    msg_makefile    =   ( "- Création des fichiers 'requierment' et "
                          "'requierment_noVers'" )
                          
    msg_filename    =   ( "- Permet de renseigner le nom du fichier" )
    
    msg_pathfile    =   ( "- Permet de renseigner le chemin du fichier" )
    
    msg_askinfo     =   ( "- Demande le non et le chemin du fichier à générer" )
    
    msg_novers      =   ( "- Permet de créer le ficher noVers à partir du fichier" )
                        
    msg_custom      =   ( "- Permet de créer le fichier 'requierment' en parcourant le "
                          "dossier donné dans 'pathfile'. Tous les fichiers portant "
                          "l’extension '.whl' seront ajoutés au fichier" )
                        
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--makefile", action='store_true', help=msg_makefile)
                        
    parser.add_argument("-f", "--filename", type=str, help=msg_filename)
                        
    parser.add_argument("-p", "--pathfile", type=str, help=msg_pathfile)
                        
    parser.add_argument("-a", "--askinfo", action='store_true', help=msg_askinfo)
                        
    parser.add_argument("--novers", action='store_true',help=msg_novers)
                             
    parser.add_argument("--custom", action='store_true', help=msg_custom)
    # parser.add_argument( "-t", "--test", action='store_true', help="activation du mode Test")
                        
    args = parser.parse_args()
    
    # print(sys.argv)
    # 'sys.argv' est une list de tous ce qui est passer comme argument à python.
    # voir : https://docs.python.org/3.6/library/sys.html
    
    # print(args)
    # présente une list de tous les arguments qui ont été ajouter avec 'add_argument'
    # et leurs état (True, False ou contenu)
    
    if args.makefile :
        print( "mode : création des fichiers\n\n" )
        i_ist = C_pipParser()
        
        v_fileName = None
        v_dirPath = None
        
        if args.askinfo :
            v_fileName = input("\tEntrez le nom du fichier : ")
            v_dirPath = input("\tEntrez le chemin du fichier à générer : ")
        else :
            if args.filename :
                v_fileName = args.filename
                
            if args.pathfile :
                v_dirPath = args.pathfile
            
        if v_fileName :
            i_ist.f_setFileName( v_fileName )
            
        if v_dirPath :
            i_ist.f_setFilePath( v_dirPath )
                   
        i_ist.f_makeRequiermentFile()
        if args.novers :
                i_ist.f_makeNoVersFile()

        if args.custom :
            i_ist.f_makeCustomFile()

    print("\n\n\t\t fin de la sequence ")    

if __name__ == '__main__':
    main()