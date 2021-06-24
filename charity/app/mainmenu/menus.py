MENUS = {
    'NAV_MENU_LEFT': [

     

        

               # another section
                {
                    "name": "Charity",
                    "url": "#",
                    "icon_class": 'mdi mdi-google-analytics',
                    "submenu": [
                        {
                    "name": "Charity  Listing Requests",
                    "url": "listrequests:requests",
                    "validators": ['menu_generator.validators.is_superuser']
                    # "validators": [
                    #             ('mainmenu.menu_validators.has_group' ,'doctor'),
                    #         ],
                            
                },
                 {
                    "name": "Donor Listing Requests",
                    "url": "listrequests:requests_donor",
                    "validators": ['menu_generator.validators.is_superuser']
                
                    # "validators": [
                    #             ('mainmenu.menu_validators.has_group' ,'doctor'),
                    #         ],
                            
                },
                {
                    "name": "Create Donation",
                    "url": "donation:create_donation",
                    "validators": [
                                ('mainmenu.menu_validators.has_group' ,'charity'),
                            
                            ],
                    
                    
                    
                },

                {
                    "name": "My Donation Requests",
                    "url": "donation:my_requests",
                    "validators": [
                                ('mainmenu.menu_validators.has_group' ,'charity'),
                            
                            ],
                    
                    
                    
                },
                {
                    "name": "All Donations",
                    "url": "donation:list_donations",
                    
                    
                    
                },
                

          
          
          
            
            ],
        },

    ]
}

