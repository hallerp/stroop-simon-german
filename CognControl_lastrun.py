#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sun Jan 16 16:49:37 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'CognControl'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ivakoncic/Desktop/Cognitive_Control/CognControl_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='Willkommen zum Experiment!\n\nUm fortzufahren, drücken Sie die LEERTASTE',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "StroopInstructions"
StroopInstructionsClock = core.Clock()
stroop_instructions = visual.TextStim(win=win, name='stroop_instructions',
    text='Sie werden nun Wörter oder Zeichen auf dem Bildschirm sehen. Diese werden jeweils in verschiedenen Farben (rot, blau, gelb) dargestellt. \n\nIhre Aufgabe ist es, so SCHNELL wie möglich anzugeben, in welcher FARBE das Wort/Zeichen abgebildet wurde. Die Person, mit der schnellsten Zeit und den wenigsten Fehlern gewinnt. \n\nDazu drücken Sie diese Tasten:\nr für ROT\ng für GELB\nb für BLAU\n\nAm besten legen Sie jetzt den linken Zeigefinger auf g, linken Mittelfinger auf r und rechten Zeigefinger auf b. So sind Sie schnell im Antworten. \n\nDrücken Sie jetzt die LEERTASTE, um einen Probedurchlauf zu starten. ',
    font='Courier New',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stroop_instruction_key = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text='\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StroopPractice"
StroopPracticeClock = core.Clock()
stroop_practice_word = visual.TextStim(win=win, name='stroop_practice_word',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stroop_practice_key = keyboard.Keyboard()

# Initialize components for Routine "stroop_practice_feedback"
stroop_practice_feedbackClock = core.Clock()
stroop_feedback_text = visual.TextStim(win=win, name='stroop_feedback_text',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "StartWarning"
StartWarningClock = core.Clock()
start_warning_text = visual.TextStim(win=win, name='start_warning_text',
    text='Achtung, jetzt geht’s richtig los! \nSie bekommen jetzt kein Feedback mehr. ',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StroopTrials"
StroopTrialsClock = core.Clock()
stroop_word = visual.TextStim(win=win, name='stroop_word',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stroop_key = keyboard.Keyboard()

# Initialize components for Routine "Done"
DoneClock = core.Clock()
done_text = visual.TextStim(win=win, name='done_text',
    text='Fertig! \n\nWeiter geht’s mit der nächsten Aufgabe. \n\nDrücken Sie die LEERTASTE, um zur Anleitung zu gelangen. ',
    font='Courier New',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
done_key = keyboard.Keyboard()

# Initialize components for Routine "SimonInstruction"
SimonInstructionClock = core.Clock()
Simon_instructions = visual.TextStim(win=win, name='Simon_instructions',
    text='Sie sehen gleich ein Viereck auf dem Bildschirm. \nIhre Aufgabe ist es, je nach FARBE (blau oder rot) des Vierecks so schnell wie möglich eine Taste zu drücken. \nAuch hier ist das Ziel möglichst schnell und möglichst viele Richtige zu haben. \n\nBlaues Viereck = Taste „s“\nRotes Viereck = Taste „k“\n\nLegen Sie jetzt am besten Ihren linken Zeigefinger auf s und rechten Zeigefinger auf k. \n\nDrücken Sie jetzt die LEERTASTE, um mit dem Probedurchlauf zu starten. ',
    font='Courier New',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
simon_instruction_key = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text='\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "SimonPractice"
SimonPracticeClock = core.Clock()
simon_practice_square = visual.ImageStim(
    win=win,
    name='simon_practice_square', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
simon_practice_key = keyboard.Keyboard()

# Initialize components for Routine "simon_practice_feedback"
simon_practice_feedbackClock = core.Clock()
simon_feedback_text = visual.TextStim(win=win, name='simon_feedback_text',
    text='',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "StartWarning"
StartWarningClock = core.Clock()
start_warning_text = visual.TextStim(win=win, name='start_warning_text',
    text='Achtung, jetzt geht’s richtig los! \nSie bekommen jetzt kein Feedback mehr. ',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FixationCross"
FixationCrossClock = core.Clock()
fix_cross = visual.TextStim(win=win, name='fix_cross',
    text='+',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "SimonTrials"
SimonTrialsClock = core.Clock()
simon_square = visual.ImageStim(
    win=win,
    name='simon_square', 
    image='sin', mask=None,
    ori=0.0, pos=[0,0], size=(0.5, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
simon_key = keyboard.Keyboard()

# Initialize components for Routine "GoodbyeScreen"
GoodbyeScreenClock = core.Clock()
Goodbyetext = visual.TextStim(win=win, name='Goodbyetext',
    text='Das war’s! \n\nDrücken Sie die LEERTASTE, um das Experiment zu beenden und sagen Sie der Experimentleiterin bescheid.',
    font='Courier New',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_goodbye = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
Welcome_resp.keys = []
Welcome_resp.rt = []
_Welcome_resp_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [Welcome_text, Welcome_resp]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        Welcome_text.setAutoDraw(True)
    
    # *Welcome_resp* updates
    waitOnFlip = False
    if Welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_resp.frameNStart = frameN  # exact frame index
        Welcome_resp.tStart = t  # local t and not account for scr refresh
        Welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_resp, 'tStartRefresh')  # time at next scr refresh
        Welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = Welcome_resp.getKeys(keyList=['space'], waitRelease=False)
        _Welcome_resp_allKeys.extend(theseKeys)
        if len(_Welcome_resp_allKeys):
            Welcome_resp.keys = _Welcome_resp_allKeys[-1].name  # just the last key pressed
            Welcome_resp.rt = _Welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome_text.started', Welcome_text.tStartRefresh)
thisExp.addData('Welcome_text.stopped', Welcome_text.tStopRefresh)
# check responses
if Welcome_resp.keys in ['', [], None]:  # No response was made
    Welcome_resp.keys = None
thisExp.addData('Welcome_resp.keys',Welcome_resp.keys)
if Welcome_resp.keys != None:  # we had a response
    thisExp.addData('Welcome_resp.rt', Welcome_resp.rt)
thisExp.addData('Welcome_resp.started', Welcome_resp.tStartRefresh)
thisExp.addData('Welcome_resp.stopped', Welcome_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StroopInstructions"-------
continueRoutine = True
# update component parameters for each repeat
stroop_instruction_key.keys = []
stroop_instruction_key.rt = []
_stroop_instruction_key_allKeys = []
# keep track of which components have finished
StroopInstructionsComponents = [stroop_instructions, stroop_instruction_key]
for thisComponent in StroopInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StroopInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StroopInstructions"-------
while continueRoutine:
    # get current time
    t = StroopInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StroopInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stroop_instructions* updates
    if stroop_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stroop_instructions.frameNStart = frameN  # exact frame index
        stroop_instructions.tStart = t  # local t and not account for scr refresh
        stroop_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stroop_instructions, 'tStartRefresh')  # time at next scr refresh
        stroop_instructions.setAutoDraw(True)
    
    # *stroop_instruction_key* updates
    waitOnFlip = False
    if stroop_instruction_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stroop_instruction_key.frameNStart = frameN  # exact frame index
        stroop_instruction_key.tStart = t  # local t and not account for scr refresh
        stroop_instruction_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stroop_instruction_key, 'tStartRefresh')  # time at next scr refresh
        stroop_instruction_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(stroop_instruction_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(stroop_instruction_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if stroop_instruction_key.status == STARTED and not waitOnFlip:
        theseKeys = stroop_instruction_key.getKeys(keyList=['space'], waitRelease=False)
        _stroop_instruction_key_allKeys.extend(theseKeys)
        if len(_stroop_instruction_key_allKeys):
            stroop_instruction_key.keys = _stroop_instruction_key_allKeys[-1].name  # just the last key pressed
            stroop_instruction_key.rt = _stroop_instruction_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StroopInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StroopInstructions"-------
for thisComponent in StroopInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stroop_instructions.started', stroop_instructions.tStartRefresh)
thisExp.addData('stroop_instructions.stopped', stroop_instructions.tStopRefresh)
# check responses
if stroop_instruction_key.keys in ['', [], None]:  # No response was made
    stroop_instruction_key.keys = None
thisExp.addData('stroop_instruction_key.keys',stroop_instruction_key.keys)
if stroop_instruction_key.keys != None:  # we had a response
    thisExp.addData('stroop_instruction_key.rt', stroop_instruction_key.rt)
thisExp.addData('stroop_instruction_key.started', stroop_instruction_key.tStartRefresh)
thisExp.addData('stroop_instruction_key.stopped', stroop_instruction_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "StroopInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [blank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank* updates
    if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank.frameNStart = frameN  # exact frame index
        blank.tStart = t  # local t and not account for scr refresh
        blank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
        blank.setAutoDraw(True)
    if blank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            blank.tStop = t  # not accounting for scr refresh
            blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
            blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blank.started', blank.tStartRefresh)
thisExp.addData('blank.stopped', blank.tStopRefresh)

# set up handler to look after randomisation of conditions etc
stroop_practice_trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stroop_practice_trials.xlsx'),
    seed=None, name='stroop_practice_trial')
thisExp.addLoop(stroop_practice_trial)  # add the loop to the experiment
thisStroop_practice_trial = stroop_practice_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStroop_practice_trial.rgb)
if thisStroop_practice_trial != None:
    for paramName in thisStroop_practice_trial:
        exec('{} = thisStroop_practice_trial[paramName]'.format(paramName))

for thisStroop_practice_trial in stroop_practice_trial:
    currentLoop = stroop_practice_trial
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_practice_trial.rgb)
    if thisStroop_practice_trial != None:
        for paramName in thisStroop_practice_trial:
            exec('{} = thisStroop_practice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(0.350000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [fix_cross]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + .35-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stroop_practice_trial.addData('fix_cross.started', fix_cross.tStartRefresh)
    stroop_practice_trial.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    
    # ------Prepare to start Routine "StroopPractice"-------
    continueRoutine = True
    # update component parameters for each repeat
    stroop_practice_word.setColor(color, colorSpace='rgb')
    stroop_practice_word.setText(word)
    stroop_practice_key.keys = []
    stroop_practice_key.rt = []
    _stroop_practice_key_allKeys = []
    # keep track of which components have finished
    StroopPracticeComponents = [stroop_practice_word, stroop_practice_key]
    for thisComponent in StroopPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StroopPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StroopPractice"-------
    while continueRoutine:
        # get current time
        t = StroopPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StroopPracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stroop_practice_word* updates
        if stroop_practice_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stroop_practice_word.frameNStart = frameN  # exact frame index
            stroop_practice_word.tStart = t  # local t and not account for scr refresh
            stroop_practice_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop_practice_word, 'tStartRefresh')  # time at next scr refresh
            stroop_practice_word.setAutoDraw(True)
        
        # *stroop_practice_key* updates
        waitOnFlip = False
        if stroop_practice_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stroop_practice_key.frameNStart = frameN  # exact frame index
            stroop_practice_key.tStart = t  # local t and not account for scr refresh
            stroop_practice_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop_practice_key, 'tStartRefresh')  # time at next scr refresh
            stroop_practice_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stroop_practice_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stroop_practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stroop_practice_key.status == STARTED and not waitOnFlip:
            theseKeys = stroop_practice_key.getKeys(keyList=['b', 'r', 'g'], waitRelease=False)
            _stroop_practice_key_allKeys.extend(theseKeys)
            if len(_stroop_practice_key_allKeys):
                stroop_practice_key.keys = _stroop_practice_key_allKeys[-1].name  # just the last key pressed
                stroop_practice_key.rt = _stroop_practice_key_allKeys[-1].rt
                # was this correct?
                if (stroop_practice_key.keys == str(correct_key)) or (stroop_practice_key.keys == correct_key):
                    stroop_practice_key.corr = 1
                else:
                    stroop_practice_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StroopPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StroopPractice"-------
    for thisComponent in StroopPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stroop_practice_trial.addData('stroop_practice_word.started', stroop_practice_word.tStartRefresh)
    stroop_practice_trial.addData('stroop_practice_word.stopped', stroop_practice_word.tStopRefresh)
    # check responses
    if stroop_practice_key.keys in ['', [], None]:  # No response was made
        stroop_practice_key.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           stroop_practice_key.corr = 1;  # correct non-response
        else:
           stroop_practice_key.corr = 0;  # failed to respond (incorrectly)
    # store data for stroop_practice_trial (TrialHandler)
    stroop_practice_trial.addData('stroop_practice_key.keys',stroop_practice_key.keys)
    stroop_practice_trial.addData('stroop_practice_key.corr', stroop_practice_key.corr)
    if stroop_practice_key.keys != None:  # we had a response
        stroop_practice_trial.addData('stroop_practice_key.rt', stroop_practice_key.rt)
    stroop_practice_trial.addData('stroop_practice_key.started', stroop_practice_key.tStartRefresh)
    stroop_practice_trial.addData('stroop_practice_key.stopped', stroop_practice_key.tStopRefresh)
    # the Routine "StroopPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stroop_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(stroop_practice_key.corr == 1):
        feedback_text = "✓"
    elif(stroop_practice_key.corr == 0):
        feedback_text = "X"
    stroop_feedback_text.setText(feedback_text)
    # keep track of which components have finished
    stroop_practice_feedbackComponents = [stroop_feedback_text]
    for thisComponent in stroop_practice_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stroop_practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stroop_practice_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stroop_practice_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stroop_practice_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stroop_feedback_text* updates
        if stroop_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stroop_feedback_text.frameNStart = frameN  # exact frame index
            stroop_feedback_text.tStart = t  # local t and not account for scr refresh
            stroop_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop_feedback_text, 'tStartRefresh')  # time at next scr refresh
            stroop_feedback_text.setAutoDraw(True)
        if stroop_feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stroop_feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                stroop_feedback_text.tStop = t  # not accounting for scr refresh
                stroop_feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stroop_feedback_text, 'tStopRefresh')  # time at next scr refresh
                stroop_feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stroop_practice_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stroop_practice_feedback"-------
    for thisComponent in stroop_practice_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stroop_practice_trial.addData('stroop_feedback_text.started', stroop_feedback_text.tStartRefresh)
    stroop_practice_trial.addData('stroop_feedback_text.stopped', stroop_feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'stroop_practice_trial'


# ------Prepare to start Routine "StartWarning"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
StartWarningComponents = [start_warning_text]
for thisComponent in StartWarningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartWarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartWarning"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StartWarningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartWarningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_warning_text* updates
    if start_warning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_warning_text.frameNStart = frameN  # exact frame index
        start_warning_text.tStart = t  # local t and not account for scr refresh
        start_warning_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_warning_text, 'tStartRefresh')  # time at next scr refresh
        start_warning_text.setAutoDraw(True)
    if start_warning_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_warning_text.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            start_warning_text.tStop = t  # not accounting for scr refresh
            start_warning_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_warning_text, 'tStopRefresh')  # time at next scr refresh
            start_warning_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartWarningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartWarning"-------
for thisComponent in StartWarningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_warning_text.started', start_warning_text.tStartRefresh)
thisExp.addData('start_warning_text.stopped', start_warning_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Stroop_trials = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StroopStim.xlsx'),
    seed=None, name='Stroop_trials')
thisExp.addLoop(Stroop_trials)  # add the loop to the experiment
thisStroop_trial = Stroop_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
if thisStroop_trial != None:
    for paramName in thisStroop_trial:
        exec('{} = thisStroop_trial[paramName]'.format(paramName))

for thisStroop_trial in Stroop_trials:
    currentLoop = Stroop_trials
    # abbreviate parameter names if possible (e.g. rgb = thisStroop_trial.rgb)
    if thisStroop_trial != None:
        for paramName in thisStroop_trial:
            exec('{} = thisStroop_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(0.350000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [fix_cross]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + .35-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Stroop_trials.addData('fix_cross.started', fix_cross.tStartRefresh)
    Stroop_trials.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    
    # ------Prepare to start Routine "StroopTrials"-------
    continueRoutine = True
    # update component parameters for each repeat
    stroop_word.setColor(color, colorSpace='rgb')
    stroop_word.setText(word)
    stroop_key.keys = []
    stroop_key.rt = []
    _stroop_key_allKeys = []
    # keep track of which components have finished
    StroopTrialsComponents = [stroop_word, stroop_key]
    for thisComponent in StroopTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StroopTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StroopTrials"-------
    while continueRoutine:
        # get current time
        t = StroopTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StroopTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stroop_word* updates
        if stroop_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stroop_word.frameNStart = frameN  # exact frame index
            stroop_word.tStart = t  # local t and not account for scr refresh
            stroop_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop_word, 'tStartRefresh')  # time at next scr refresh
            stroop_word.setAutoDraw(True)
        
        # *stroop_key* updates
        waitOnFlip = False
        if stroop_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stroop_key.frameNStart = frameN  # exact frame index
            stroop_key.tStart = t  # local t and not account for scr refresh
            stroop_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop_key, 'tStartRefresh')  # time at next scr refresh
            stroop_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stroop_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stroop_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stroop_key.status == STARTED and not waitOnFlip:
            theseKeys = stroop_key.getKeys(keyList=['r', 'b', 'g'], waitRelease=False)
            _stroop_key_allKeys.extend(theseKeys)
            if len(_stroop_key_allKeys):
                stroop_key.keys = _stroop_key_allKeys[-1].name  # just the last key pressed
                stroop_key.rt = _stroop_key_allKeys[-1].rt
                # was this correct?
                if (stroop_key.keys == str(correct_key)) or (stroop_key.keys == correct_key):
                    stroop_key.corr = 1
                else:
                    stroop_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StroopTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StroopTrials"-------
    for thisComponent in StroopTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Stroop_trials.addData('stroop_word.started', stroop_word.tStartRefresh)
    Stroop_trials.addData('stroop_word.stopped', stroop_word.tStopRefresh)
    # check responses
    if stroop_key.keys in ['', [], None]:  # No response was made
        stroop_key.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           stroop_key.corr = 1;  # correct non-response
        else:
           stroop_key.corr = 0;  # failed to respond (incorrectly)
    # store data for Stroop_trials (TrialHandler)
    Stroop_trials.addData('stroop_key.keys',stroop_key.keys)
    Stroop_trials.addData('stroop_key.corr', stroop_key.corr)
    if stroop_key.keys != None:  # we had a response
        Stroop_trials.addData('stroop_key.rt', stroop_key.rt)
    Stroop_trials.addData('stroop_key.started', stroop_key.tStartRefresh)
    Stroop_trials.addData('stroop_key.stopped', stroop_key.tStopRefresh)
    # the Routine "StroopTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'Stroop_trials'


# ------Prepare to start Routine "Done"-------
continueRoutine = True
# update component parameters for each repeat
done_key.keys = []
done_key.rt = []
_done_key_allKeys = []
# keep track of which components have finished
DoneComponents = [done_text, done_key]
for thisComponent in DoneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DoneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Done"-------
while continueRoutine:
    # get current time
    t = DoneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DoneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done_text* updates
    if done_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_text.frameNStart = frameN  # exact frame index
        done_text.tStart = t  # local t and not account for scr refresh
        done_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_text, 'tStartRefresh')  # time at next scr refresh
        done_text.setAutoDraw(True)
    
    # *done_key* updates
    waitOnFlip = False
    if done_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_key.frameNStart = frameN  # exact frame index
        done_key.tStart = t  # local t and not account for scr refresh
        done_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_key, 'tStartRefresh')  # time at next scr refresh
        done_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(done_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(done_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if done_key.status == STARTED and not waitOnFlip:
        theseKeys = done_key.getKeys(keyList=['space'], waitRelease=False)
        _done_key_allKeys.extend(theseKeys)
        if len(_done_key_allKeys):
            done_key.keys = _done_key_allKeys[-1].name  # just the last key pressed
            done_key.rt = _done_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Done"-------
for thisComponent in DoneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('done_text.started', done_text.tStartRefresh)
thisExp.addData('done_text.stopped', done_text.tStopRefresh)
# check responses
if done_key.keys in ['', [], None]:  # No response was made
    done_key.keys = None
thisExp.addData('done_key.keys',done_key.keys)
if done_key.keys != None:  # we had a response
    thisExp.addData('done_key.rt', done_key.rt)
thisExp.addData('done_key.started', done_key.tStartRefresh)
thisExp.addData('done_key.stopped', done_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "Done" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SimonInstruction"-------
continueRoutine = True
# update component parameters for each repeat
simon_instruction_key.keys = []
simon_instruction_key.rt = []
_simon_instruction_key_allKeys = []
# keep track of which components have finished
SimonInstructionComponents = [Simon_instructions, simon_instruction_key]
for thisComponent in SimonInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SimonInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SimonInstruction"-------
while continueRoutine:
    # get current time
    t = SimonInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SimonInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Simon_instructions* updates
    if Simon_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Simon_instructions.frameNStart = frameN  # exact frame index
        Simon_instructions.tStart = t  # local t and not account for scr refresh
        Simon_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Simon_instructions, 'tStartRefresh')  # time at next scr refresh
        Simon_instructions.setAutoDraw(True)
    
    # *simon_instruction_key* updates
    waitOnFlip = False
    if simon_instruction_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        simon_instruction_key.frameNStart = frameN  # exact frame index
        simon_instruction_key.tStart = t  # local t and not account for scr refresh
        simon_instruction_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(simon_instruction_key, 'tStartRefresh')  # time at next scr refresh
        simon_instruction_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(simon_instruction_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(simon_instruction_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if simon_instruction_key.status == STARTED and not waitOnFlip:
        theseKeys = simon_instruction_key.getKeys(keyList=['space'], waitRelease=False)
        _simon_instruction_key_allKeys.extend(theseKeys)
        if len(_simon_instruction_key_allKeys):
            simon_instruction_key.keys = _simon_instruction_key_allKeys[-1].name  # just the last key pressed
            simon_instruction_key.rt = _simon_instruction_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SimonInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SimonInstruction"-------
for thisComponent in SimonInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Simon_instructions.started', Simon_instructions.tStartRefresh)
thisExp.addData('Simon_instructions.stopped', Simon_instructions.tStopRefresh)
# check responses
if simon_instruction_key.keys in ['', [], None]:  # No response was made
    simon_instruction_key.keys = None
thisExp.addData('simon_instruction_key.keys',simon_instruction_key.keys)
if simon_instruction_key.keys != None:  # we had a response
    thisExp.addData('simon_instruction_key.rt', simon_instruction_key.rt)
thisExp.addData('simon_instruction_key.started', simon_instruction_key.tStartRefresh)
thisExp.addData('simon_instruction_key.stopped', simon_instruction_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "SimonInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [blank]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank* updates
    if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank.frameNStart = frameN  # exact frame index
        blank.tStart = t  # local t and not account for scr refresh
        blank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
        blank.setAutoDraw(True)
    if blank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            blank.tStop = t  # not accounting for scr refresh
            blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
            blank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('blank.started', blank.tStartRefresh)
thisExp.addData('blank.stopped', blank.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Simon_practice_trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Simon_stim.xlsx'),
    seed=None, name='Simon_practice_trials')
thisExp.addLoop(Simon_practice_trials)  # add the loop to the experiment
thisSimon_practice_trial = Simon_practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSimon_practice_trial.rgb)
if thisSimon_practice_trial != None:
    for paramName in thisSimon_practice_trial:
        exec('{} = thisSimon_practice_trial[paramName]'.format(paramName))

for thisSimon_practice_trial in Simon_practice_trials:
    currentLoop = Simon_practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSimon_practice_trial.rgb)
    if thisSimon_practice_trial != None:
        for paramName in thisSimon_practice_trial:
            exec('{} = thisSimon_practice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(0.350000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [fix_cross]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + .35-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Simon_practice_trials.addData('fix_cross.started', fix_cross.tStartRefresh)
    Simon_practice_trials.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    
    # ------Prepare to start Routine "SimonPractice"-------
    continueRoutine = True
    # update component parameters for each repeat
    simon_practice_square.setPos((pos, 0))
    simon_practice_square.setImage(square)
    simon_practice_key.keys = []
    simon_practice_key.rt = []
    _simon_practice_key_allKeys = []
    # keep track of which components have finished
    SimonPracticeComponents = [simon_practice_square, simon_practice_key]
    for thisComponent in SimonPracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SimonPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SimonPractice"-------
    while continueRoutine:
        # get current time
        t = SimonPracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SimonPracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *simon_practice_square* updates
        if simon_practice_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            simon_practice_square.frameNStart = frameN  # exact frame index
            simon_practice_square.tStart = t  # local t and not account for scr refresh
            simon_practice_square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(simon_practice_square, 'tStartRefresh')  # time at next scr refresh
            simon_practice_square.setAutoDraw(True)
        
        # *simon_practice_key* updates
        waitOnFlip = False
        if simon_practice_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            simon_practice_key.frameNStart = frameN  # exact frame index
            simon_practice_key.tStart = t  # local t and not account for scr refresh
            simon_practice_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(simon_practice_key, 'tStartRefresh')  # time at next scr refresh
            simon_practice_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(simon_practice_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(simon_practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if simon_practice_key.status == STARTED and not waitOnFlip:
            theseKeys = simon_practice_key.getKeys(keyList=['s', 'k'], waitRelease=False)
            _simon_practice_key_allKeys.extend(theseKeys)
            if len(_simon_practice_key_allKeys):
                simon_practice_key.keys = _simon_practice_key_allKeys[-1].name  # just the last key pressed
                simon_practice_key.rt = _simon_practice_key_allKeys[-1].rt
                # was this correct?
                if (simon_practice_key.keys == str(correct_key)) or (simon_practice_key.keys == correct_key):
                    simon_practice_key.corr = 1
                else:
                    simon_practice_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SimonPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SimonPractice"-------
    for thisComponent in SimonPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Simon_practice_trials.addData('simon_practice_square.started', simon_practice_square.tStartRefresh)
    Simon_practice_trials.addData('simon_practice_square.stopped', simon_practice_square.tStopRefresh)
    # check responses
    if simon_practice_key.keys in ['', [], None]:  # No response was made
        simon_practice_key.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           simon_practice_key.corr = 1;  # correct non-response
        else:
           simon_practice_key.corr = 0;  # failed to respond (incorrectly)
    # store data for Simon_practice_trials (TrialHandler)
    Simon_practice_trials.addData('simon_practice_key.keys',simon_practice_key.keys)
    Simon_practice_trials.addData('simon_practice_key.corr', simon_practice_key.corr)
    if simon_practice_key.keys != None:  # we had a response
        Simon_practice_trials.addData('simon_practice_key.rt', simon_practice_key.rt)
    Simon_practice_trials.addData('simon_practice_key.started', simon_practice_key.tStartRefresh)
    Simon_practice_trials.addData('simon_practice_key.stopped', simon_practice_key.tStopRefresh)
    # the Routine "SimonPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simon_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(simon_practice_key.corr == 1):
        feedback_text2 = "✓"
    elif(simon_practice_key.corr == 0):
        feedback_text2 = "X"
    simon_feedback_text.setText(feedback_text2)
    # keep track of which components have finished
    simon_practice_feedbackComponents = [simon_feedback_text]
    for thisComponent in simon_practice_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    simon_practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "simon_practice_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = simon_practice_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=simon_practice_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *simon_feedback_text* updates
        if simon_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            simon_feedback_text.frameNStart = frameN  # exact frame index
            simon_feedback_text.tStart = t  # local t and not account for scr refresh
            simon_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(simon_feedback_text, 'tStartRefresh')  # time at next scr refresh
            simon_feedback_text.setAutoDraw(True)
        if simon_feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > simon_feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                simon_feedback_text.tStop = t  # not accounting for scr refresh
                simon_feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(simon_feedback_text, 'tStopRefresh')  # time at next scr refresh
                simon_feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simon_practice_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simon_practice_feedback"-------
    for thisComponent in simon_practice_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Simon_practice_trials.addData('simon_feedback_text.started', simon_feedback_text.tStartRefresh)
    Simon_practice_trials.addData('simon_feedback_text.stopped', simon_feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'Simon_practice_trials'


# ------Prepare to start Routine "StartWarning"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
StartWarningComponents = [start_warning_text]
for thisComponent in StartWarningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartWarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartWarning"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StartWarningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartWarningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_warning_text* updates
    if start_warning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_warning_text.frameNStart = frameN  # exact frame index
        start_warning_text.tStart = t  # local t and not account for scr refresh
        start_warning_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_warning_text, 'tStartRefresh')  # time at next scr refresh
        start_warning_text.setAutoDraw(True)
    if start_warning_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_warning_text.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            start_warning_text.tStop = t  # not accounting for scr refresh
            start_warning_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_warning_text, 'tStopRefresh')  # time at next scr refresh
            start_warning_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartWarningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartWarning"-------
for thisComponent in StartWarningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_warning_text.started', start_warning_text.tStartRefresh)
thisExp.addData('start_warning_text.stopped', start_warning_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Simon_trials = data.TrialHandler(nReps=21.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Simon_stim.xlsx'),
    seed=None, name='Simon_trials')
thisExp.addLoop(Simon_trials)  # add the loop to the experiment
thisSimon_trial = Simon_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSimon_trial.rgb)
if thisSimon_trial != None:
    for paramName in thisSimon_trial:
        exec('{} = thisSimon_trial[paramName]'.format(paramName))

for thisSimon_trial in Simon_trials:
    currentLoop = Simon_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSimon_trial.rgb)
    if thisSimon_trial != None:
        for paramName in thisSimon_trial:
            exec('{} = thisSimon_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixationCross"-------
    continueRoutine = True
    routineTimer.add(0.350000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationCrossComponents = [fix_cross]
    for thisComponent in FixationCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixationCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + .35-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixationCross"-------
    for thisComponent in FixationCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Simon_trials.addData('fix_cross.started', fix_cross.tStartRefresh)
    Simon_trials.addData('fix_cross.stopped', fix_cross.tStopRefresh)
    
    # ------Prepare to start Routine "SimonTrials"-------
    continueRoutine = True
    # update component parameters for each repeat
    simon_square.setPos((pos, 0))
    simon_square.setImage(square)
    simon_key.keys = []
    simon_key.rt = []
    _simon_key_allKeys = []
    # keep track of which components have finished
    SimonTrialsComponents = [simon_square, simon_key]
    for thisComponent in SimonTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SimonTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SimonTrials"-------
    while continueRoutine:
        # get current time
        t = SimonTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SimonTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *simon_square* updates
        if simon_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            simon_square.frameNStart = frameN  # exact frame index
            simon_square.tStart = t  # local t and not account for scr refresh
            simon_square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(simon_square, 'tStartRefresh')  # time at next scr refresh
            simon_square.setAutoDraw(True)
        
        # *simon_key* updates
        waitOnFlip = False
        if simon_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            simon_key.frameNStart = frameN  # exact frame index
            simon_key.tStart = t  # local t and not account for scr refresh
            simon_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(simon_key, 'tStartRefresh')  # time at next scr refresh
            simon_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(simon_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(simon_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if simon_key.status == STARTED and not waitOnFlip:
            theseKeys = simon_key.getKeys(keyList=['s', 'k'], waitRelease=False)
            _simon_key_allKeys.extend(theseKeys)
            if len(_simon_key_allKeys):
                simon_key.keys = _simon_key_allKeys[-1].name  # just the last key pressed
                simon_key.rt = _simon_key_allKeys[-1].rt
                # was this correct?
                if (simon_key.keys == str(correct_key)) or (simon_key.keys == correct_key):
                    simon_key.corr = 1
                else:
                    simon_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SimonTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SimonTrials"-------
    for thisComponent in SimonTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Simon_trials.addData('simon_square.started', simon_square.tStartRefresh)
    Simon_trials.addData('simon_square.stopped', simon_square.tStopRefresh)
    # check responses
    if simon_key.keys in ['', [], None]:  # No response was made
        simon_key.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           simon_key.corr = 1;  # correct non-response
        else:
           simon_key.corr = 0;  # failed to respond (incorrectly)
    # store data for Simon_trials (TrialHandler)
    Simon_trials.addData('simon_key.keys',simon_key.keys)
    Simon_trials.addData('simon_key.corr', simon_key.corr)
    if simon_key.keys != None:  # we had a response
        Simon_trials.addData('simon_key.rt', simon_key.rt)
    Simon_trials.addData('simon_key.started', simon_key.tStartRefresh)
    Simon_trials.addData('simon_key.stopped', simon_key.tStopRefresh)
    # the Routine "SimonTrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 21.0 repeats of 'Simon_trials'


# ------Prepare to start Routine "GoodbyeScreen"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
key_goodbye.keys = []
key_goodbye.rt = []
_key_goodbye_allKeys = []
# keep track of which components have finished
GoodbyeScreenComponents = [Goodbyetext, key_goodbye]
for thisComponent in GoodbyeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GoodbyeScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GoodbyeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Goodbyetext* updates
    if Goodbyetext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Goodbyetext.frameNStart = frameN  # exact frame index
        Goodbyetext.tStart = t  # local t and not account for scr refresh
        Goodbyetext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Goodbyetext, 'tStartRefresh')  # time at next scr refresh
        Goodbyetext.setAutoDraw(True)
    if Goodbyetext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Goodbyetext.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            Goodbyetext.tStop = t  # not accounting for scr refresh
            Goodbyetext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Goodbyetext, 'tStopRefresh')  # time at next scr refresh
            Goodbyetext.setAutoDraw(False)
    
    # *key_goodbye* updates
    waitOnFlip = False
    if key_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_goodbye.frameNStart = frameN  # exact frame index
        key_goodbye.tStart = t  # local t and not account for scr refresh
        key_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_goodbye, 'tStartRefresh')  # time at next scr refresh
        key_goodbye.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_goodbye.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_goodbye.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_goodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_goodbye.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            key_goodbye.tStop = t  # not accounting for scr refresh
            key_goodbye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_goodbye, 'tStopRefresh')  # time at next scr refresh
            key_goodbye.status = FINISHED
    if key_goodbye.status == STARTED and not waitOnFlip:
        theseKeys = key_goodbye.getKeys(keyList=['space'], waitRelease=False)
        _key_goodbye_allKeys.extend(theseKeys)
        if len(_key_goodbye_allKeys):
            key_goodbye.keys = _key_goodbye_allKeys[-1].name  # just the last key pressed
            key_goodbye.rt = _key_goodbye_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GoodbyeScreen"-------
for thisComponent in GoodbyeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Goodbyetext.started', Goodbyetext.tStartRefresh)
thisExp.addData('Goodbyetext.stopped', Goodbyetext.tStopRefresh)
# check responses
if key_goodbye.keys in ['', [], None]:  # No response was made
    key_goodbye.keys = None
thisExp.addData('key_goodbye.keys',key_goodbye.keys)
if key_goodbye.keys != None:  # we had a response
    thisExp.addData('key_goodbye.rt', key_goodbye.rt)
thisExp.addData('key_goodbye.started', key_goodbye.tStartRefresh)
thisExp.addData('key_goodbye.stopped', key_goodbye.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
