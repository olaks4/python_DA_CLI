def studentprofile():
    name = input('enter your name')
    age =input('enter your age')


    print(f'student name is {name}, student is {age} years old')

    # studentprofile()

    def personprofile(name, age,location):
        print(f'student name is {name}')
        print(f{student lives at {location}})

        #personprofile('bukola',16, 'ibadan')
        #personprofile('samuel', 87, 'lagos')

        ##################################

        '''
        oop object oriented programmming
        python class/project
        
        Human being
        Attribute, name , age , gender, hair_color , height, weight, profession
        methods/Actions- running , eating, sing...

        Car
        Attributes -color ,name , model , type , speed , manufacturer, manufacturing_data
        Action- car-type, honk
        

        School
        Attributes - name , location, students , teacher;
        methods- teach
        '''

        class Car():

            def __init__(self, name, model, max_speed, colo, manufacturer):
                self.name = name 
                self.model = model
                self.max_speed= max_speed
                self.colo= colo 
                self.manufacturer =manufactuerer

            def car_type(self):
                '''
                speed <100=normal car

                speed (100-150) = modern car
                speed (151- 200)= exotic car
                speed (200-250)= muscle car
                speed (250- 300) =sport car
                speed >= 301 = super car

                '''

                if self.max_spped >= 301:
                    print (f'The {self.name.capitalize()} car is a super car')
                elif self.max_spped >= 250:
                    print (f'The {self.name.capitalize()} car is a sportcar')
                elif self.max_spped >= 200:
                    print (f'The {self.name.capitalize()} car is a musclecar')
                elif self.max_spped >= 151:
                    print (f'The {self.name.capitalize()} car is a exotic car')
                elif self.max_spped >= 100:
                    print (f'The {self.name.capitalize()} car is a modern car')
                else:
                    print(f'the {self.name.capitalize()} car is a normal  car')



car1 = car()
                    
 
