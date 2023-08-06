# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 02:20:52 2021

@author: Mostafa
"""


#import matplotlib.pyplot as plt
import matplotlib as mpl
#import numpy as np

#%%
plt_to_tex_marker={
        'None': 'None',
        's': 'square*',
        'o': '*',
        '^': 'triangle*',
        'd': 'diamond*',
        '*': 'x',
        '.': '*,'
        }
plt_to_tex_linestyle={
        'None': 'only marks',
        ':': 'dotted',
        '--': 'dashed',
        '-': 'solid',
#        '^': 'triangle*'
        }
#%%
def savetex(pathname,save_type='pic'):
#    x=np.linspace(0,4*np.pi,1000)
#    y=np.cos(x)
    mpl_gca=mpl.pyplot.gca()
    
#    picture_name='some_test'
    num_of_lines=len(mpl_gca.lines)
    
#    print(num_of_lines)
    
    tex_title=mpl_gca.title.get_text()
    tex_xlabel=mpl_gca.xaxis.get_label().get_text()
    tex_ylabel=mpl_gca.yaxis.get_label().get_text()
    tex_xlim=mpl_gca.get_xlim()
    tex_ylim=mpl_gca.get_ylim()
    tex_xticks=','.join([str(u) for u in mpl_gca.get_xticks()])
    tex_yticks=','.join([str(u) for u in mpl_gca.get_yticks()])
    temp_tex_legends=mpl_gca.get_legend_handles_labels()
    tex_legends={
            mpl_gca.lines.index(temp_tex_legends[0][n]):temp_tex_legends[1][n]\
            for n in range(len(temp_tex_legends[0]))
            }
    
    tex_xy_data=[]
    tex_marker=[]
    tex_markersize=[]
    tex_linestyle=[]
    tex_linecolor=[]
    tex_linewidth=[]
    for line in mpl_gca.lines:
        temp_xy_data=list(zip(line.get_xdata(),line.get_ydata()))
        tex_xy_data.append(''.join([str(xy) for xy in temp_xy_data]))
        tex_marker.append(plt_to_tex_marker[line.get_marker()])
        tex_markersize.append(line.get_markersize()*0.4)
        tex_linestyle.append(plt_to_tex_linestyle[line.get_linestyle()])
        tex_linecolor.append(mpl.colors.to_hex(line.get_color())[1:].upper())
        tex_linewidth.append(line.get_linewidth())
    
    has_tex_title=not tex_title==''
    has_tex_xlabel=not tex_xlabel==''
    has_tex_ylabel=not tex_ylabel==''
    
    file=open(pathname+'.tex','w+')
    
    if save_type=='full':
        file.writelines('\\documentclass{article}\n')
        file.writelines('\\usepackage{tikz,pgfplots}\n')
        file.writelines('\\begin{document}\n')
    
    for n in range(num_of_lines):
        file.writelines('\\definecolor{{color{}}}{{HTML}}{{{}}}\n'.format(n,tex_linecolor[n]))
    file.writelines('\\begin{tikzpicture}\n')
    file.writelines('\\begin{axis}\n')
    file.writelines('[\n')
    file.writelines('\ttitle = {{{}}},\n'.format(tex_title)*has_tex_title)
    file.writelines('\txlabel = {{{}}},\n'.format(tex_xlabel)*has_tex_xlabel)
    file.writelines('\tylabel = {{{}}},\n'.format(tex_ylabel)*has_tex_ylabel)
    file.writelines('\txmin = {{{}}},\n'.format(tex_xlim[0]))
    file.writelines('\txmax = {{{}}},\n'.format(tex_xlim[1]))
    file.writelines('\tymin = {{{}}},\n'.format(tex_ylim[0]))
    file.writelines('\tymax = {{{}}},\n'.format(tex_ylim[1]))
    file.writelines('\txtick = {{{}}},\n'.format(tex_xticks))
    file.writelines('\tytick = {{{}}},\n'.format(tex_yticks))
    file.writelines(']\n')
    
    for n in range(num_of_lines):
        file.writelines('\\addplot\n')
        file.writelines('[\n')
        file.writelines('\t{},\n'.format(tex_linestyle[n]))
        file.writelines('\tmark={},\n'.format(tex_marker[n]))
        file.writelines('\tmark size={},\n'.format(tex_markersize[n]))
        file.writelines('\tcolor=color{},\n'.format(n))
        file.writelines('\tline width={}pt,\n'.format(tex_linewidth[n]))
        file.writelines(']\n')
        file.writelines('coordinates{\n')
        file.writelines(tex_xy_data[n])
        file.writelines('\n};\n')
    
    if not tex_legends=={}:
        file.writelines('\\legend{\n')
        for n in range(num_of_lines):
            if n in tex_legends:
                file.writelines('\t{{{}}},\n'.format(tex_legends[n]))
            else:
                file.writelines('\t{},\n')
        file.writelines('}\n')
    
    file.writelines('\\end{axis}\n')
    file.writelines('\\end{tikzpicture}\n')
    
    if save_type=='full':
        file.writelines('\\end{document}')
    
    file.close()
    return