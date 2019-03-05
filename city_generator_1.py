import maya.cmds as cm
import random

def chooseHeight(_proxCentre, _cityDropOff, _maxHeight):
	'''this function calculates the height of a building, 
	depending on how far away it is from the city centre 
	and what the user has in putted as the city drop off.
	It returns the height.'''
	
	_heightProb=(_proxCentre+_cityDropOff)/2.0
	_modeHeight=_maxHeight*_heightProb
	height=(random.triangular(2, _maxHeight, _modeHeight))
	return height     
    
		
					
def makeBuilding0(_buildingName, _buildArea, _numOfLevels, shader):
	'''This function creates building 0 '''

	for i in range (_numOfLevels):
		cm.polyCube(w=1, h=0.8, d=1, name= str(_buildingName) + str(i) + '*')
		cm.move(0,i+0.4,0)
		
		cm.polyCube(w=0.8, h=0.2, d=0.88, name=str(_buildingName) + str(i) + '*')
		cm.move(0,i+0.9,0)
		
		cm.polyUnite(str(_buildingName) + str(i) + '*', n=str(_buildingName)+'*')	

        cm.polyUnite(str(_buildingName) + '*', n=str(_buildingName))
        cm.sets(str(_buildingName), edit=True, forceElement=shader)
	cm.scale(_buildArea[0], 1, _buildArea[1])			
	
		
def makeBuilding1(_buildingName, _buildArea, _numOfLevels, shader):
	'''This function creates building 1 '''
	
	for i in range (_numOfLevels):
		cm.polyCylinder(r=0.5, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.0625, 0)
		
		cm.polyCylinder(r=0.45, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.1875, 0)
					
		cm.polyCylinder(r=0.5, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.3125, 0)
		
		cm.polyCylinder(r=0.45, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.4375, 0)
		
		cm.polyCylinder(r=0.5, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.5625, 0)
		
		cm.polyCylinder(r=0.45, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.6875, 0)
		
		cm.polyCylinder(r=0.5, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.8125, 0)
		
		cm.polyCylinder(r=0.45, h=0.125, name=str(_buildingName) + str(i) + '*')
		cm.move(0, i+0.9375, 0)
		
		cm.polyUnite(str(_buildingName) + str(i) + '*', n=str(_buildingName)+'*')	
		
		
	cm.polyUnite(str(_buildingName) + '*', n=str(_buildingName))	
        cm.sets(str(_buildingName), edit=True, forceElement=shader)
	cm.scale(_buildArea[0], 1, _buildArea[1])
				    
				    
def makeBuilding2(_buildingName, _buildArea, _numOfLevels, shader):
	'''This function creates building 2 '''
	
	for i in range (_numOfLevels):
		if i==_numOfLevels-1:
			cm.polyCube(w=1, h=0.5, d=0.6, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.25,0)
						
			cm.polyCube(w=0.6, h=0.5, d=1, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.25,0)
						
			cm.polyCube(w=0.8, h=0.2, d=0.5, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.5,0)
						
			cm.polyCube(w=0.5, h=0.2, d=0.8, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.5,0)
			
						
		else:
			cm.polyCube(w=1, h=0.5, d=0.6, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.25,0)
						
			cm.polyCube(w=0.6, h=0.5, d=1, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.25,0)
						
			cm.polyCube(w=0.7, h=0.5, d=0.4, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.75,0)
						
			cm.polyCube(w=0.4, h=0.5, d=0.7, n= str(_buildingName) + str(i) + '*')
			cm.move(0,i+0.75,0)
		
		cm.polyUnite(str(_buildingName) + str(i) + '*', n=str(_buildingName)+'*')
	
	cm.polyUnite(str(_buildingName) + '*', n=str(_buildingName))
        cm.sets(str(_buildingName), edit=True, forceElement=shader)
	cm.scale(_buildArea[0], 1, _buildArea[1])
	
	
	
def makeBuilding3(_buildingName, _buildArea, _numOfLevels, shader):
	'''This function creates building 3 '''
	
	cm.polyCube(w=1, h=0.2, d=1, n = str(_buildingName) + '*')
	cm.move(0, 0.1, 0)
		
	cm.polyCube(w=1, h=0.2, d=1, name= str(_buildingName) + '*')
	cm.move(0, 0.1+_numOfLevels, 0)
			
	cm.polyCube(w=0.143, h=_numOfLevels, d=0.143, name= str(_buildingName) + '*')
	cm.move(0.429, float(_numOfLevels)/2, 0.429)

	cm.polyCube(w=0.143, h=_numOfLevels, d=0.143, name= str(_buildingName) + '*')
	cm.move(0.429, float(_numOfLevels)/2, -0.429)

	cm.polyCube(w=0.143, h=_numOfLevels, d=0.143, name= str(_buildingName) + '*')
	cm.move(-0.429, float(_numOfLevels)/2, 0.429)
		
	cm.polyCube(w=0.143, h=_numOfLevels, d=0.143, name= str(_buildingName) + '*')
	cm.move(-0.429, float(_numOfLevels)/2, -0.429)

	cm.polyCube(w=0.143, h=_numOfLevels, d=1, name= str(_buildingName) + '*')
	cm.move(0.143, float(_numOfLevels)/2, 0)

	cm.polyCube(w=0.143, h=_numOfLevels, d=1, name= str(_buildingName) + '*')
	cm.move(-0.143, float(_numOfLevels)/2, 0)

	cm.polyCube(w=1, h=_numOfLevels, d=0.143, name= str(_buildingName) + '*')
	cm.move(0, float(_numOfLevels)/2, 0.143)

	cm.polyCube(w=1, h=_numOfLevels, d=0.143, name= str(_buildingName) + '*')
	cm.move(0, float(_numOfLevels)/2, -0.143)
		
	cm.polyUnite(str(_buildingName) + '*', n=str(_buildingName))
        cm.sets(str(_buildingName), edit=True, forceElement=shader)
	cm.scale(_buildArea[0], 1, _buildArea[1])
	
	
def makeBuilding4(_buildingName, _buildArea, _numOfLevels, shader):
	'''This function creates building 4 '''
	
	cm.polyPrism(ns=5, w=0.6, l=float(_numOfLevels)/2, n=str(_buildingName)+'*')
	cm.move(0, float(_numOfLevels)/4, 0)
	cm.polyPrism(ns=5, w=0.5, l=float(_numOfLevels)/4, n=str(_buildingName)+'*')
	cm.move(0, 5*float(_numOfLevels)/8, 0)
	cm.polyPrism(ns=5, w=0.4, l=float(_numOfLevels)/4, n=str(_buildingName)+'*')
	cm.move(0, 7*float(_numOfLevels)/8, 0) 
	
	cm.polyUnite(str(_buildingName) + '*', n=str(_buildingName))
        cm.sets(str(_buildingName), edit=True, forceElement=shader)
	cm.scale(_buildArea[0], 1, _buildArea[1]) 	
	

def makeCityBuilding(_buildingName, _buildArea, _numOfLevels, setName):
	'''This function chooses which building to make,
	it is choosen randomly.'''

	_chooseBuilding=random.randint(0, 4)
        _chooseColour=random.randint(2, 8)
        shader = setName[_chooseColour]
	
	if _chooseBuilding==0:
                makeBuilding0(_buildingName, _buildArea, _numOfLevels, shader)
	elif _chooseBuilding==1:
                makeBuilding1(_buildingName, _buildArea, _numOfLevels, shader)
	elif _chooseBuilding==2:
                makeBuilding2(_buildingName, _buildArea, _numOfLevels, shader)
	elif _chooseBuilding==3:
                makeBuilding3(_buildingName, _buildArea, _numOfLevels, shader)
	elif _chooseBuilding==4:
                makeBuilding4(_buildingName, _buildArea, _numOfLevels, shader)
	else:
		print 'Oops! Something has gone wrong! Value assigned to _chooseBuilding is not in range'	




def makeVegetation(_buildingName, _buildArea, _height, setName):
	'''This function makes a tree
	
	The tree is made of 2 parts the trunk and the leaves.
	The height of the tree is generated randomly.'''
	
	_heightTrunk=_height*random.uniform(0.1,0.5)
	_heightLeaf=_height-_heightTrunk
	
	cm.polyCylinder(n=str(_buildingName)+'trunk', sx=8, r=0.2, h=_heightTrunk) 
	cm.move(0,_heightTrunk/2.0, 0, str(_buildingName)+'trunk')
        cm.sets(str(_buildingName)+'trunk', edit=True, forceElement=setName[0])
	
	_leafType=random.randint(0, 1)
	_radius=random.uniform(0.4, 0.5)
	
	
        cm.polyCone(n= str(_buildingName)+'leaf', r=_radius, sx=12, h=_heightLeaf)
	cm.move(0,_heightTrunk+_heightLeaf/2.0, 0, str(_buildingName)+'leaf')
        cmds.sets(str(_buildingName)+'leaf', edit=True, forceElement=setName[1])
        cm.group(str(_buildingName) + 'trunk', str(_buildingName)+'leaf', n=str(_buildingName))

	

	
def makeSuburbObject(_buildingName, _buildArea, _cityDropOff, _proxCentre, setName):
	'''This function decides which object to place in 
	a suburb block: a tree, a building or blank (grass)'''
	
	_vegProb = 1 - (random.random()*_proxCentre*3)
	treeheight = random.uniform(2,4)
	cityheight=random.uniform(2, 6)
	
	if _vegProb < 0.3:
                makeCityBuilding(_buildingName, _buildArea, int(cityheight), setName)
	if _vegProb > 0.8:
                makeVegetation(_buildingName, _buildArea, treeheight, setName)
			
	
def makeRegularBlock(_blockName, _cityDropOff, _gap, _amountBuild, _buildArea, _maxHeight, _proxCentre, _blockSize, setName):
	"""This procedure makes a block with a grid of buildings.
	
	There are two for loops which run through the amount of 
	buildings in the x and z direction of a block. With the for loop 
	the building or vegetation is made and place in the right position.
        It is parented to the plane which all elements of the block lie on.
        """
	
	for x in range (_amountBuild):
		for z in range (_amountBuild):
		    
			_buildingName=str(_blockName) + '_building_' +str(x)+str(z) 
			
			_XDim = random.uniform(0.5, _buildArea)
			_ZDim = random.uniform(0.5, _buildArea)
			_area = (_XDim, _ZDim)	

			_numOfLevels=int(chooseHeight(_proxCentre, _cityDropOff, _maxHeight))
			
			_gapSize=_gap[0]+_gap[1]
			_divisionSize=_blockSize /_amountBuild
			
			#determines whether a suburb building or a skyscraper should be made.
			if _proxCentre>_cityDropOff:
                                makeCityBuilding(_buildingName, _area, _numOfLevels, setName)
			else:
                                makeSuburbObject(_buildingName, _area, _cityDropOff, _proxCentre, setName)

                        if (cm.objExists(_buildingName)):
                            cm.move(x*_divisionSize + _divisionSize/2.0, 0, z*_divisionSize + _divisionSize/2.0, _buildingName)
                            cm.parent(_buildingName, _blockName)
							
	ang= random.choice([0, 90])
	cm.rotate(0, ang, 0, _blockName)
	
def makeShaders():

	colourList = []
        colour1 = (0.5, 0.25, 0.1)
        colourList.append(colour1)
        colour2 = (0, 0.5, 0)
        colourList.append(colour2)
        colour3 = (0.09, 0.104, 0.114)
        colourList.append(colour3)
        colour4 = (0.228,0.317,0.310)
        colourList.append(colour4)
        colour5 = (0.226, 0.26, 0.271)
        colourList.append(colour5)
        colour6 = (0.062, 0.09, 0.1)
        colourList.append(colour6)
        colour7 = (0.271, 0.271, 0.26)
        colourList.append(colour7)
        colour8 = (0.482, 0.539, 0.504)
        colourList.append(colour8)
        colour9 = (0.136, 0.140, 0.125)
        colourList.append(colour9)

        setName = []
        for i in range(9):
            setName.append(cmds.sets(name='_MaterialGroup_', renderable=True, empty=True))
            greenShader=cm.shadingNode("lambert", asShader=True, n='shader'+str(i))
            cm.setAttr(greenShader+'.color', colourList[i][0], colourList[i][1], colourList[i][2], type='double3')
            cmds.surfaceShaderList('shader'+str(i), add=setName[i])


        return setName
	

def makeCity(_numBlocks, _cityDropOff, _gap, _amountBuild, _buildArea, _maxHeight):
	"""This procedure moves the city blocks to the right position in the city.
	
	It has 7 parameters:
	_numBlocks,      integer,      the number of blocks in each the x and z direction of the city
	_cityDropOff,    float,        a ratio of how quickly the inner city fades into the suburbs
	_gap,            tuple,        information of how large the distance is between buildings which affects the size of the block
	_amountBuild,    integer,      the number of buildings in a block which affects the size of the block
	_buildArea,      float,        the how large an area each building takes up which affects the size of the block
	_maxHeight,      integer,      the maximum height a building can be
	
	In terms of building the city this is the top function. From the values in the parameters, other variables such as the block size, 
	the centre point of the city, the maximum distance a block can be translated from the centre to the edge.
	
	2 for loops are then set up to go through the number of blocks in the x axis and the z axis. Within the for loops the displacement 
	the current block is made and moved."""
	
	#Calulate the block size 
	_blockSize =(_amountBuild)*(_buildArea +_gap[0]+_gap[1])
	
	#Calulate centre point of the city
	_centrePt = _blockSize*_numBlocks*0.5
	
	#Calulate the distance of the blocks at the corners of the city
        _maxDist =((_centrePt)**2 + (_centrePt)**2)**0.5

	setName=makeShaders()

	for x in range (_numBlocks):
		for z in range (_numBlocks):
			
			#Calcuate current position of block (x, y, z)
			_currentTrans=(x*_blockSize, 0, z*_blockSize)
			
			#Calculate current distance of block from the centre 
			_currentDist=(((_centrePt-_currentTrans[0])**2)+((_centrePt-_currentTrans[2])**2))**0.5
			
			#Calculate a ratio of the current distance over the maximum distance (1 minus this ratio, so large number closer to the centre)
			_proxCentre=1-(_currentDist/_maxDist)
			
			#Make block and move to the right position
			_blockName='block_' + str(x) +str(z)
			
			cm.polyPlane(n=str(_blockName), sx=1, sy=1, h=_blockSize, w=_blockSize)
			cm.move(_blockSize/2, 0, _blockSize/2)
			
                        makeRegularBlock(_blockName, _cityDropOff, _gap, _amountBuild, _buildArea, _maxHeight, _proxCentre, _blockSize, setName)
				
			cm.move(_currentTrans[0], 0, _currentTrans[2],str(_blockName))
			cm.refresh(f=True)
				


				
def start():
    """This procedure gets the values from the sliders and buttons and passes them into the function makeCity
    
    It has no parameters and returns nothing.
    
    This procedure calls deleteCity function to clear the scene and then queries all the buttons and sliders for their values and assigns
    them to appropiate variables which are then passed as arguments into the function makeCity."""		
    
    #Call function to delete everything in the scene
    #In case the user has not already deleted the previous city built.
    deleteCity()     
    
  
    _numBlocks=cm.intSliderGrp('blockSlider', query = True, value=True)
    _cityDropOff = cm.floatSliderGrp('innercitySlider', query = True, value = True)
    _roadSize = cm.floatSliderGrp('roadWidthSlider', query = True, value = True)
    _paveSize = cm.floatSliderGrp('paveWidthSlider', query = True, value = True) 
    _amountBuild = cm.intSliderGrp('buildPerBlockSlider', query = True, value = True)
    _buildArea = cm.floatSliderGrp('areaBuilding', query = True, value = True)
    _maxHeight= cm.intSliderGrp('heightSlider', query = True, value = True)    
   
    
    #Put the road size and pavement size (multipled by two because inbetween 2 buildings there are 2 pavements) into one tuple
    _gap=(_paveSize*2, _roadSize) 
    
    makeCity(_numBlocks, _cityDropOff, _gap, _amountBuild, _buildArea, _maxHeight)
    
    
  
def _intOnDrag(name):
    """This procedure changes the background colour of the integer slider group depending on its value. 
    
    It has one parameter, which is the name of the integer slider group.
    
    The value is assigned to the variable "value", which is then used to determine what the background colour should be. If the value is 
    within a good range then it turns green, if it is in an okay range it turns amber and if it is in a risky range it turns red."""
    
    value=cm.intSliderGrp(name, query = True, value=True)
    
    if value>2 and value<12:
        cm.intSliderGrp(name, edit = True, bgc=(0.3, 0.7, 0.3)) 
    if value>12 and value<20:
        cm.intSliderGrp(name, edit = True, bgc=(0.9, 0.4, 0.1)) 
    if value>20:
        cm.intSliderGrp(name, edit = True, bgc=(0.9, 0.2, 0.2))  
        
    
def createLayout():
	"""This procedure creates the layout of the user interface. 
	
        It has no parameters and returns nothing.
	
	The layout of the user interface is then created with the appropiate buttons and sliders; ranges are specified to prevent the user 
	from breaking the program. I have allowed fairly large ranges that will probably take Maya quite a long time to create as I do not 
	want to limit the user too much. However, with certain variables such as the number of blocks in the city and the density of the 
	buildings I have warned the user of that there is a slight risk that Maya might crash by having the background colour of the sliders 
	change according to the user input. When the button "Delete City" is clicked the function "deleteCity" is called. When the button 
	"Make City" is clicked the function "start" is called."""


	cm.columnLayout(adjustableColumn = True, rowSpacing = 5, cw=100, cal = 'left')
		
	cm.frameLayout( label='Attributes of City' )
        #Number of blocks in the city - this will affect the size of the city
        cm.intSliderGrp('blockSlider', field = True, label = "Number Of Blocks", v = 8, min = 1, max = 30)
	cm.intSliderGrp('blockSlider', edit = True, dc='_intOnDrag("blockSlider")')        
        #Slider for the size of the inner city, it controls the spread of the buildings
        #i.e. at value 0 there will be more vegetation and at 1 there will be more buildings
	cm.floatSliderGrp('innercitySlider', field = True, label = "Size Of Inner City", v = 0.9, min = 0, max = 1, fs = 0.1)
        #Slider for the width of the road
	cm.floatSliderGrp('roadWidthSlider', field = True, label = "Size Of Road", v = 0.1, min = 0, max = 5, fs = 0.1)
        #Slider for the width of the pavement
	cm.floatSliderGrp('paveWidthSlider', field = True, label = "Size Of Pavements", v = 0.1, min = 0, max = 2, fs = 0.1)
	cm.setParent( '..' )
	

	cm.frameLayout( label='Attributes of Buildings' )
        #Slider for the number of buildings in a block, this will affect the size of each block
	cm.intSliderGrp('buildPerBlockSlider', field = True, label = "Density Of Buildings", v = 7, min = 1, max = 10, fs = 0.1)
        #Slider for the size of buildings in a block, this will affect the size of each block
	cm.floatSliderGrp('areaBuilding', field = True, label = "Area Of Buildings", v = 0.5, min = 0, max = 1, fs = 0.1)
        #Slider for the maximum height of buildings
	cm.intSliderGrp('heightSlider', field = True, label = "Maximum Height Of Buildings", v = 10, min = 5, max = 20, fs = 0.1)
	cm.setParent( '..' )
	
	cm.rowColumnLayout(numberOfColumns = 2, columnWidth = [(1, 200), (2, 200)])
        #Buttons to start making the city or delete the current city built.
	cm.button(label = "Delete City", width = 150, align = 'center', command = 'deleteCity()')
	cm.button(label = "Make City", width = 150, align = 'center', command = 'start()')
    
    
def deleteCity():
    """This function deletes everything in the scene.
    
    It has no parameters and returns nothing."""
    cm.select(all = True)
    cm.delete()
    
def createUI():
	"""This procedure creates the user interface.
	
        It has no parameters and returns nothing.
	
	It initally checks if there is a current window of the same name already open and if so, it deletes it. It then creates the window
	and calls the function createLayout. The last line reveals the window created to the user """
	
	_cityBuildWindow = "City_Builder"
        #Checks if there is an existing window open and closes it
	if cm.window(_cityBuildWindow, exists=True):
	    cm.deleteUI(_cityBuildWindow)

        #Creates window
	cm.window(_cityBuildWindow, title = 'City Generator', wh = (400, 500), s = True)
        #Creates layout of window
	createLayout()
        #Displays window on screen
	cm.showWindow(_cityBuildWindow)
    
if __name__ == "__main__":    
    createUI()
    
