#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Infos
=====

   :Projet:             pipParser
   :Nom du fichier:     pipParser.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170513

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.6
    
####

Descriptif
==========

    :Projet:            Ce petit programe permet de créer 2 fichiers requierement pour
                        l'intallation des paquet sous python.

                        Le premier est le fichier classique. Le second fichier est
                        débarrasser des numéro de version qui accompagne chacun des
                        paquet dans le premier fichier..

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
   
"""

from __future__ import absolute_import
import os, sys
sys.path.insert(0,'..')         # ajouter le repertoire precedent au path (non définitif)
                                # pour pouvoir importer les modules et paquets parent
    
import argparse

class C_pipParser( object ) :
    def __init__( self) :
        """ **__init__()**
        
            Creation et initialisation des variables globales de cette Class
        """
        self._v_dir             = os.getcwd()
                                    # os.getcwd() : permet de recuperer le chemin
                                    # du repertoire local
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
                
            *N.B :* Si l'instance n'est plus utilisee, cette methode est appellee 
            automatiquement.
        """
        ## Action
        v_className = self.__class__.__name__
        
####

    def f_setFilePath(self, v_localWorkDir=None) :
        """ Permet de définir le chemin dans lequel est créé le fichier. Ce chemin est
            utilisé comme repertoire de travail (workdir).
        """
        ## Action
        if v_localWorkDir :
            self._v_dir = os.path.normpath(v_localWorkDir)
            os.chdir(self._v_dir)
                # permet de déclarer '_v_dir' comme répertoire courrant
        else :
            print( "Acun chemin n'a été spécifié. le chemin par défaut sera utilisé" /       " : \n {}".format(self._v_dir)
                 )
                
####
                
    def f_getFilePath(self) :
        """ Retourne le chemin dans lequel est créer le fichier.
        
            **N.B** : Ce chemin correspond au répertoire courrant (workdir).
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
                   "Le nom du fichiers sans version sera : {1}".format(
                   self._v_fileName, self._v_fileNameNoVers
                   )
                 )
        else :
            self._v_fileName = "{}.txt".format(v_fileName)
            self._v_fileNameNoVers = "{}_noVers.txt".format(v_fileName)
            self._v_customFile = "{}_custom.txt".format(v_fileName)

####

    def f_getFileName(self) :
        """ Retourne le nom des fichiers avec et sans version sous la forme d'un tuple
        """
        return (self._v_fileName, self._v_fileNameNoVers)
            
####

    def f_setFullFileName(self) :
        """ Permet définir les fichiers et leur chemin sous la forme d'un tuple 
            comportant deux string composées de cette façon : ::
        
                [chemin_du_fichier]\[nom_du_fichier]
        """
        ## Action
        self._t_fullFileName = (
                                    os.path.join(self._v_dir, self._v_fileName),
                                    os.path.join(self._v_dir, self._v_fileNameNoVers),
                                    os.path.join(self._v_dir, self._v_customFile)
                                )
        
####
            
    def f_getFullFileName(self) :
        """ Retourne le Nom des fichiers précédés de leur chemin (retourne un tuple).
        """
        ## Action
        return self._t_fullFileName

####

    def f_makeRequiermentFile(self, v_dirPath=None, v_fileName=None) :
        """ Permet de créer le fichier requierement de pip freeze. la commande qui va
            être executée sera : ::
            
                pip3 freeze > [nom_du_fichier]
                
            v_dirPath : Permet de définir le chemin dans lequel est créé le fichier.
            Ce chemin est utilisé comme repertoire de travail (workdir). Si il est définie, la méthode 'f_setFilePath()' sera appellée.
            
            v_fileName : Permet de définir le nom du fichier. Si il est définie, la
            méthode 'f_setFileName()' sera appellée.
            
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
                                    
    def f_makeCustomFile( self ) :
        """ Permet de créer le fichier 'requierment' en parcourant le dossier '_v_dir'.
            Tous les fichiers portant l'extention '.whl' seront ajoutés au fichier
            '_v_customFile'
        """
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
                            
                            Le premier fichier est le fichier générer par la commande 
                            pip3 freeze > nom_du_fichier. Le second fichier générer est
                            une copie du premier nettoyer des numéros de versions. Ce
                            second fichier sera nomé de la même façon que le premier
                            avec le suffixe '_noVers' en plus.
                            
        :arg filename:      -f ou --filename. Permet de spécifier le nom du fichier.
                            Ce nom doit être spécifier sans pathfile l'extension car
                            l'extension '.txt' sera automatiquement ajouté.
                            
        :arg pathfile:      -p ou --pathfile. Permet de spécifier le chemin d'accès
                            des fichiers.
                            
        :arg askinfo:       -a ou --askinfo. Lance une invite de commande pour remplir
                            le nom du fichier et son chemin d'accès.
                            
                            Si l'un des arguments 'filename' ou 'pathfile' et passé en
                            même temp que 'askinfo', ils seront ignoré.
                            
                            Si aucun nom ou chemin n'est renseigné dans l'invite de
                            commande, le nom du fichier par défaut sera :
                            'myRequierment' et le chemin par défaut sera le répertoire
                            courrant( '.' ).
    """
    msg_makefile    =   ( "- Création des fichiers 'requierment' et "
                          "'requierment_noVers'" )
                          
    msg_filename    =   ( "- Permet de renseigner le nom du fichier" )
    
    msg_pathfile    =   ( "- Permet de renseigner le chemin du fichier" )
    
    msg_askinfo     =   ( "- Demande le non et le chemin du fichier à générer" )
    
    msg_novers      =   ( "- Permet de créer le ficher noVers à partir du fichier" )
                        
    msg_custom      =   ( "- Permet de créer le fichier 'requierment' en parcourant le "
                          "dossier donné dans 'pathfile'. Tous les fichiers portant "
                          "l'extention '.whl' seront ajoutés au fichier" )
                        
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
    # print(args)
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
