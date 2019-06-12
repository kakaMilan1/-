#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import *
import tkinter
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from model import Model
from gevent.pywsgi import WSGIServer
import logging

app = Flask(__name__)
CORS(app)

vocab_file = 'data/dl-data/couplet/vocabs'
model_dir = 'data/dl-data/models/tf-lib/output_couplet'

m = Model(
        None, None, None, None, vocab_file,
        num_units=1024, layers=4, dropout=0.2,
        batch_size=32, learning_rate=0.0001,
        output_dir=model_dir,
        restore_model=True, init_train=False, init_infer=True)

top = Tk()
L1 = Label(top, text="请输入上联")
L1.grid(row=0,column=0)
L2 = Label(top, text="下联")
L2.grid(row=1,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=0,column=1)
listB=Entry(top)
listB.grid(row=1,column=1)

def CallRun():
    listB.delete(0,END)
    in_str=E1.get()
    output = m.infer(' '.join(in_str))
    output = ''.join(output.split(' '))
    listB.insert(0,output)

B = tkinter.Button(top, text ="点击生成", command = CallRun);
B.grid(row=3,column=3,rowspan=2,columnspan=2)

top.mainloop()
