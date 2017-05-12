#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             pipParser
   :Nom du fichier:     pipParser.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170512

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
                                    os.path.join(self._v_dir, self._v_fileNameNoVers)
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
            
                pip freeze > [nom_du_fichier]
                
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
        os.system( "pip freeze > {}".format(self.f_getFullFileName()[0]) )
        
####
        
    def f_makeNoVersFile( self ) :
        """ Permet de créer le ficher noVers à partir du fichier générer par pip
        """
        ## Action
        v_xIndex = 0
        v_charIndex = 0
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

def main() :
    """ Fonction principale """
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--makefile", action='store_true',
                        help="Création des fichiers 'reqierment' et 'requierment_noVers'\n")
    parser.add_argument("-f", "--filename", type=str,
                        help="permet de renseigner le nom du fichier")
    parser.add_argument("-p", "--pathfile", type=str,
                        help="permet de renseigner le chemin du fichier")
    parser.add_argument("-a", "--askinfo", action='store_true',
                        help="demande le non et le chemin du fichier à générer")
    # parser.add_argument( "-t", "--test", action='store_true', help="activation du mode Test")
                        
    args = parser.parse_args()
    
    print(args)
    
    if args.makefile :
        print( "mode : création des fichiers\n\n" )
        i_ist = C_pipParser()
        
        v_fileName = None
        v_dirPath = None
        
        if args.askinfo :
            v_fileName = input("\tEntrez le nom du fichier : ")
            v_dirPath = input("\tEntrez le chemin du fichier à générer : ")
            
        if args.filename :
            v_fileName = args.filename
            
        if args.pathfile :
            v_dirPath = args.pathfile
            
        if v_fileName :
            i_ist.f_setFileName( v_fileName )
            
        if v_dirPath :
            i_ist.f_setFilePath( v_localWorkDir )
            
        i_ist.f_makeRequiermentFile()
        i_ist.f_makeNoVersFile()
        


    print("\n\n\t\t fin de la sequence ")    

if __name__ == '__main__':
    main()
