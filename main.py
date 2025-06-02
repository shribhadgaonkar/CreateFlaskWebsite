# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 05:34:58 2025

@author: shrib
"""

from website import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000,use_reloader = False)     #evertime i make change in py file .. It will re run 
    
    
    