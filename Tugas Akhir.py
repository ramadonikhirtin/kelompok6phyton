# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

<p><img alt="Colaboratory logo" height="45px" src="/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px"></p>

<h1>What is Colaboratory?</h1>

Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser, with 
- Zero configuration required
- Free access to GPUs
- Easy sharing

Whether you're a **student**, a **data scientist** or an **AI researcher**, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more, or just get started below!

## **Getting started**

The document you are reading is not a static web page, but an interactive environment called a **Colab notebook** that lets you write and execute code.

For example, here is a **code cell** with a short Python script that computes a value, stores it in a variable, and prints the result:
"""

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

"""To execute the code in the above cell, select it with a click and then either press the play button to the left of the code, or use the keyboard shortcut "Command/Ctrl+Enter". To edit the code, just click the cell and start editing.

Variables that you define in one cell can later be used in other cells:
"""

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

"""Colab notebooks allow you to combine **executable code** and **rich text** in a single document, along with **images**, **HTML**, **LaTeX** and more. When you create your own Colab notebooks, they are stored in your Google Drive account. You can easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To learn more, see [Overview of Colab](/notebooks/basic_features_overview.ipynb). To create a new Colab notebook you can use the File menu above, or use the following link: [create a new Colab notebook](http://colab.research.google.com#create=true).

Colab notebooks are Jupyter notebooks that are hosted by Colab. To learn more about the Jupyter project, see [jupyter.org](https://www.jupyter.org).

## Data science

With Colab you can harness the full power of popular Python libraries to analyze and visualize data. The code cell below uses **numpy** to generate some random data, and uses **matplotlib** to visualize it. To edit the code, just click the cell and start editing.
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""You can import your own data into Colab notebooks from your Google Drive account, including from spreadsheets, as well as from Github and many other sources. To learn more about importing data, and how Colab can be used for data science, see the links below under [Working with Data](#working-with-data).

## Machine learning

With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just [a few lines of code](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb). Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including [GPUs and TPUs](#using-accelerated-hardware), regardless of the power of your machine. All you need is a browser.

Colab is used extensively in the machine learning community with applications including:
- Getting started with TensorFlow
- Developing and training neural networks
- Experimenting with TPUs
- Disseminating AI research
- Creating tutorials

To see sample Colab notebooks that demonstrate machine learning applications, see the [machine learning examples](#machine-learning-examples) below.

## More Resources

### Working with Notebooks in Colab
- [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb)
- [Guide to Markdown](/notebooks/markdown_guide.ipynb)
- [Importing libraries and installing dependencies](/notebooks/snippets/importing_libraries.ipynb)
- [Saving and loading notebooks in GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Interactive forms](/notebooks/forms.ipynb)
- [Interactive widgets](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [TensorFlow 2 in Colab](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### Working with Data
- [Loading data: Drive, Sheets, and Google Cloud Storage](/notebooks/io.ipynb) 
- [Charts: visualizing data](/notebooks/charts.ipynb)
- [Getting started with BigQuery](/notebooks/bigquery.ipynb)

### Machine Learning Crash Course
These are a few of the notebooks from Google's online Machine Learning course. See the [full course website](https://developers.google.com/machine-learning/crash-course/) for more.
- [Intro to Pandas](/notebooks/mlcc/intro_to_pandas.ipynb)
- [Tensorflow concepts](/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
- [First steps with TensorFlow](/notebooks/mlcc/first_steps_with_tensor_flow.ipynb)
- [Intro to neural nets](/notebooks/mlcc/intro_to_neural_nets.ipynb)
- [Intro to sparse data and embeddings](/notebooks/mlcc/intro_to_sparse_data_and_embeddings.ipynb)

<a name="using-accelerated-hardware"></a>
### Using Accelerated Hardware
- [TensorFlow with GPUs](/notebooks/gpu.ipynb)
- [TensorFlow with TPUs](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## Machine Learning Examples

To see end-to-end examples of the interactive machine learning analyses that Colaboratory makes possible, check out these  tutorials using models from [TensorFlow Hub](https://tfhub.dev).

A few featured examples:

- [Retraining an Image Classifier](https://tensorflow.org/hub/tutorials/tf2_image_retraining): Build a Keras model on top of a pre-trained image classifier to distinguish flowers.
- [Text Classification](https://tensorflow.org/hub/tutorials/tf2_text_classification): Classify IMDB movie reviews as either *positive* or *negative*.
- [Style Transfer](https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization): Use deep learning to transfer style between images.
- [Multilingual Universal Sentence Encoder Q&A](https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa): Use a machine learning model to answer questions from the SQuAD dataset.
- [Video Interpolation](https://tensorflow.org/hub/tutorials/tweening_conv3d): Predict what happened in a video between the first and the last frame.
"""

#Metode Setengah Interval (MODUL 2)

print('''
Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
====Metode Setengah Interval====''')


X1 = float(input("Nilai Pertama: "))
X2 = float(input("Nilai Kedua: "))
error = 1
iterasi = 0
while(error > 0.0001):
    iterasi +=1
    FXi = 0.0533*(X1**3)-5.5006*(X1**2)+140.4*(X1)-1020.1
    FXii = 0.0533*(X2**3)-5.5006*(X2**2)+140.4*(X2)-1020.1
    Xt = (X1 + X2)/2
    FXt = 0.0533*(Xt**3)-5.5006*(Xt**2)+140.4*(Xt)-1020.1
    if FXi * FXt > 0:
        X1 = Xt
    elif FXi * FXt < 0:
        X2 = Xt
    else:
        print("Akar Penyelesaian: ", Xt)
    if FXt < 0:
        error = FXt * (-1)
    else:
        error = FXt
    if iterasi > 100:
        print("Angka tak hingga")
        break
    print(iterasi, "|", FXi, "|", FXii, "|", Xt, "|", FXt, "|", error)
print("Jumlah Iterasi: ", iterasi)
print("Akar persamaan adalah: ", Xt)
print("Toleransi Error: ", error)

Metode Interpolasi Linier (MODUL 2)

print('''
Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
====Metode Interpolasi Linier====''')


X1 = float(input("Masukkan Nilai Pertama: "))
X2 = X1 + 1
error = 1
iterasi = 0
while(error > 0.0001):
    iterasi +=1
    FX1 = 0.0533*(X1**3)-5.5006*(X1**2)+140.4*(X1)-1020.1
    FX2 = 0.0533*(X2**3)-5.5006*(X2**2)+140.4*(X2)-1020.1
    Xt = X2 - ((FX2/(FX2-FX1)))*(X2-X1)
    FXt = 0.0533*(Xt**3)-5.5006*(Xt**2)+140.4*(Xt)-1020.1
    if FXt*FX1 > 0:
        X2 = Xt
        FX2 = FXt
    else:
        X1 = Xt
        FX1 = FXt
    if FXt < 0:
        error = FXt * (-1)
    else:
        error = FXt
    if iterasi > 500:
        print("Angka tak hingga")
        break
    print(iterasi, "|", FX1, "|", FX2, "|", Xt, "|", FXt, "|", error)
print("Jumlah Iterasi: ", iterasi)
print("Akar persamaan adalah: ", Xt)
print("Toleransi Error: ", error)

#Metode Secant (MODUL 2)

print('''
Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
====Metode Secant====''')


X1 = float(input("Masukkan Nilai Pertama: "))
X2 = X1 - 1
error = 1
iterasi = 0
while(error > 0.0001):
    iterasi +=1
    FX1 = 0.0533*(X1**3)-5.5006*(X1**2)+140.4*(X1)-1020.1
    FXmin = 0.0533*(X2**3)-5.5006*(X2**2)+140.4*(X2)-1020.1
    X3 = X1 - ((FX1)*(X1-(X2)))/((FX1)-(FXmin))
    FXplus = 0.0533*(Xt**3)-5.5006*(Xt**2)+140.4*(Xt)-1020.1
    if FXplus < 0:
        error = FXplus * (-1)
    else:
        error = FXplus
    if error > 0.0001:
        X2 = X1
        X1 = X3
    else:
        print("Selesai")
    if iterasi > 500:
        print("Angka tak hingga")
        break
    print(iterasi, "|", FX1, "|", FXmin, "|", X3, "|", FXplus, "|", error)
print("Jumlah Iterasi: ", iterasi)
print("Akar persamaan adalah: ", X3)
print("Toleransi Error: ", error)

#Metode Newton-Rhapson (MODUL 2)

print('''
Nama : Pramesthi Dwi O
NIM : 26050119130086
Kelas : Oseanografi B
====Metode Newton-Rhapson====''')


X1 = float(input("Masukkan Nilai Pertama: "))
iterasi = 0
akar = 1
while (akar > 0.0001):
    iterasi += 1
    Fxn = 0.0533*(X1**3)-5.5006*(X1**2)+140.4*(X1)-1020.1
    Fxxn = ((3*0.0533)*(X1**2))-((2*5.5006)*X1)+140.4
    xnp1 = X1 - (Fxn/Fxxn)
    fxnp1 = (xnp1**3)+(xnp1**2)-(3*xnp1)-3
    Ea = ((xnp1-X1)/xnp1)*100
    if Ea < 0.0001:
        X1 = xnp1
        akar = Ea*(-1)
    else:
        akar = xnp1
        print("Nilai akar adalah: ", akar)
        print("Nilai error adalah: ", Ea)
    if iterasi > 100:
        break
    print(iterasi, "|", X1, "|", xnp1, "|", akar, "|", Ea)
print("Jumlah Iterasi: ", iterasi)
print("Akar persamaan adalah: ", xnp1)
print("Toleransi Error: ", akar)

#Metode Iterasi (MODUL 2)

print('''
Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
====Metode Iterasi====''')


X1 = float(input("Masukkan Nilai Pertama: "))
error = 1
iterasi = 0
while (error > 0.0001):
    iterasi +=1
    Fxn = 0.0533*(X1**3)-5.5006*(X1**2)+140.4*(X1)-1020.1
    X2 = ((5.5006*(X1**2)-140.4*(X1)+1020.1)/0.0533)**(0.333334)
    Ea = (((X2-X1)/(X2))*100)
    if Ea < error:
        X1 = X2
        if Ea > 0:
            error = Ea
        else:
            error = Ea*(-1)
    else:
        error = Ea
    if iterasi > 100:
        print("Angka tak hingga")
        break
    print(iterasi, "|", X1, "|", X2, "|", Ea, "|", error)
print("Jumlah Iterasi: ", iterasi)
print("Akar persamaan adalah: ", X2)
print("Toleransi Error: ", error)

#PERHITUNGAN METODE ELEMINASI GAUSS (MODUL 3)

print (""""Nama : Pramesthi Dwi O\n
NIM : 26050119130086\n
Kelas : Oseanografi B\n
Metode Gauss\n""")

#Diketahui
#5x1 + 10x2 + 3x3 + 8x4 = 4.886
#1x1 + 5x2 + 6x3 + 6x4 = 9.086
#2x1 + 3x2 + 5x3 + 4x4 = 20.086
#3x1 + 6x2 + 6x3 + 5x4 = 10.086

import numpy as np

def Cal_LU_pivot(D, g):
    A = np.array((D), dtype=float)
    f = np.array((g), dtype=float)
    n = len(f)
    for i in range(0, n - 1):  # Looping untuk kolom matriks

        if np.abs(A[i, i]) == 0:
            for k in range(i + 1, n):
                if np.abs(A[k, i]) > np.abs(A[i, i]):
                    A[[i, k]] = A[[k, i]]  # Tukar antara baris i dan k
                    f[[i, k]] = f[[k, i]]
                    break

        for j in range(i + 1, n):  # Ulangi baris di bawah diagonal untuk setiap kolom
            m = A[j, i] / A[i, i]
            A[j, :] = A[j, :] - m * A[i, :]
            f[j] = f[j] - m * f[i]
    return A, f


A = np.array([[5,10,3,8], [1,5,6,6], [2,3,5,4], [3,6,6,5]], dtype=float)
f = np.array([4.886, 9.086, 20.086, 10.086])
print('A = \n%s and f = %s' % (A, f))
B, g = Cal_LU_pivot(A, f)
x = np.linalg.solve(A, f)
print('Hasil perhitungan gauss adalah x = \n %s' % x)

#PERHITUNGAN METODE ELEMINASI GAUSS JORDAN (MODUL 3)

print (""""Nama : Pramesthi Dwi O\n
NIM : 26050119130086\n
Kelas : Oseanografi B\n
Metode Gauss Jordan\n""")

#Diketahui
#5x1 + 10x2 + 3x3 + 8x4 = 4.886
#1x1 + 5x2 + 6x3 + 6x4 = 9.086
#2x1 + 3x2 + 5x3 + 4x4 = 20.086
#3x1 + 6x2 + 6x3 + 5x4 = 10.086

import numpy as np
import sys

def GaussJordan(a,n):
    #Step1 ===> Looping untuk pengolahan metode Gauss Jordan
    print('==============Mulai Iterasi===============')
    for i in range(n):
        if a[i][i]==0:
            sys.exit('Dibagi dengan angka nol (proses tidak dapat dilanjutkan)')
        for j in range(n):
            if i !=j:
                ratio=a[j][i]/a[i][i]
                #print('posisi nol di:[',j,i,']', 'nilai rasio:',ratio)
                
                for k in range (n+1):
                    a[j,k]=a[j][k]-ratio*a[i][k]
                print(a)
                print(f'============================================')
    # Step 2 ====> Membuat semua variabel(x,y,z,...)==1
    ax=np.zeros((n,n+1))
    for i in range(n):
        for j in range(n+1):
            ax[i,j]=a[i][j]/a[i][i]
    print('===================Akhir Iterasi============')
    return ax

m = np.array([[5,10,3,8,4.886],
             [1,5,6,6,9.086],
             [2,3,5,4,20.086],
             [3,6,6,5,10.086]],dtype=float)
n = 4

# Menampilkan matrix awal
print('Matriks Persamaan')
print(m)

# Menampilkan Hasil
m = GaussJordan(m,n)
print(f"""Hasil Pengolahan menggunakan metode Gauss Jordan didapatkan matriks:
{m}""")

#PERHITUNGAN METODE ITERASI GAUSS SIEDEL (MODUL 3)

print (""""Nama : Pramesthi Dwi O\n
NIM : 26050119130086\n
Kelas : Oseanografi B\n
Metode Gauss Siedel\n""")

import numpy as np 
from scipy.linalg import solve 

def GaussSeidel (A, b, x, n):
    L = np.tril(A)
    U = A -L
    for i in range(n):
        x=np.dot(np.linalg.inv(L), b - np.dot(U,x))
        print (f'Iterasi Ke-{str(i+1).zfill(3)}'),
        print (x)
    return x

#Masukan
A= np.array([[5,10,3,8],
             [1,5,6,6],
             [2,3,5,4],
             [3,6,6,5]],dtype=float)
b=[4.886, 9.086, 20.086, 10.086]
x=np.zeros_like(b)
n=25

H= GaussSeidel(A, b, x, n)
K= solve(A,b)

print(f'Hasil pengerjaan menggunakan Gauss Seidel didapatkan nilai tiap variabel {H}')
print(f'Variabel matriks menggunakan SciPy {K}')

#PERHITUNGAN METODE ITERASI GAUSS JACOBI (MODUL 3)

print (""""Nama : Pramesthi Dwi O\n
NIM : 26050119130086\n
Kelas : Oseanografi B\n
Metode Gauss Jacobi\n""")

import numpy as np
from scipy.linalg import solve

def jacobi(A,b,x,n):
  D = np.diag(A)
  R = A-np.diagflat(D)
  for i in range(n):
    x = (b-np.dot(R,x))/D
    print (f'Iterasi Ke-{str(i+1).zfill(3)}'),
    print (x)
  return x

A= np.array([[5,10,3,8],
             [1,5,6,6],
             [2,3,5,4],
             [3,6,6,5]])
b=[4.886, 9.086, 20.086, 10.086]

x = [1.0,1.0,1.0,1.0]
n = 25
J = jacobi(A,b,x,n)
O = solve(A,b)
print(f'Hasil pengerjaan menggunakan Jacobi didapatkan nilai tiap variabel {J}')
print(f'Variabel matriks menggunakan SciPy {O}')

#METODE TRAPESIUM BANYAK PIAS (MODUL 4)

print('''
Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
=====Tugas Metode Numerik Modul 4=====
=====Trapesium Banyak Pias=====''')

import math
import numpy as np
from matplotlib import pyplot as plt

def trapesium(f,a,b,N):
    x = np.linspace(a,b,N+1)
    y = f(x)
    y_right = y[1:] 
    y_left = y[:-1] 
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

f = lambda x : 3*(x**3) + 4*(x**2) + 6
a = 3
b = 4
N = 6

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b+1,N)
Y = f(X)
plt.plot(X,Y)

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

plt.title('Trapesium banyak pias, N = {}'.format(N))
plt.show()

L = trapesium(f,a,b,N)
print(L)

#METODE TRAPESIUM 1 PIAS (MODUL 4)

Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
=====Tugas Metode Numerik Modul 4=====
=====Trapesium 1 Pias=====''')

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10,100)
y= x**2
plt.plot(x,y)

x1 = 0
x2 = 1
fx1 = x1**2
fx2 =x2**2

plt.fill_between([x1,x2],[fx1,fx2])

plt.xlim([-1.5,1.5]); plt.ylim([0,1.5]);
plt.title('Trapesium 1 pias')
plt.show()

L = 0.5*(fx2 + fx1)*(x2 - x1)
print("Luas dengan metode trapesium 1 pias :", L)

#MEODE SIMPSON 3/8 (MODUL 4)

Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
=====Tugas Metode Numerik Modul 4=====
=====Simpson 3/8=====''')

def f(x):
    return 4+2*math.sin(x)

def simpson3per8(x0,xn,n):
    h = (xn - x0) / n
    
    integral = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integral = integral + 3 * f(k)
        else:
            integral = integral + 3 * f(k)
    
    integral = integral * 3 * h / 8
    
    return integral
    
x1 = float(input("batas bawah (x1): "))
x2 = float(input("batas atas (x2) kudu nulis dalam kelipatan 3.14: "))

hasil = simpson3per8(x1, x2, 3)
print("nilai integral metode Simpson 3/8:", hasil )

#Simpson 1/3 (MODUL 4)

print('''
Nama : Pramesthi Dwi Octavianna
NIM : 26050119130086
Kelas : Oseanografi B
=====Tugas Metode Numerik Modul 4=====
=====Simpson 1/3=====''')

def f(x):
    return 3*(x**3)+4*(x**2)+6

def simpson1per3(x0,xn,n):
    h = (xn - x0) / n
    
    integral = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integral = integral + 2 * f(k)
        else:
            integral = integral + 4 * f(k)
    
    integral = integral * h/3
    
    return integral
    
x1 = float(input("batas bawah (x1): "))
x2 = float(input("batas atas (x2): "))

hasil = simpson1per3(x1, x2, 2)
print("nilai integral metode Simpson 1/3:",hasil )

#METODE EULER (MODUL 5)
print("Nama : Pramesthi Dwi Octavianna \n",
     "NIM : 6050119130086 \n",
     "Kelas : Oseanografi B \n")

#=== Import Library ===#
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
get_ipython().run_line_magic('matplotlib', 'inline')

#==== Mendefinisikan parameter dan fungsi ===#
h = float(input("Masukkan nilai h: ")) # Step size
x0 = float(input("Masukkan nilai x awal: "))
xn = float(input("Masukkan nilai x akhir: "))
x = np.arange(x0, xn + h, h) # Numerical grid
y0 = float(input("Masukkan nilai y awal: ")) # Initial Condition
G = 2*((x**3)) + 9*(x**2) + 3*(x) + 86
f = lambda x, y: 2*((x**3)) + 9*(x**2) + 3*(x) + 86 # Persamaan Differensial Biasa


#=== Metode Euler Eksplisit ===#
y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h*f(x[i], y[i])
    
print(y)

#=== Menghitung Error ===#
Galat = G-y
print (Galat)

#=== Menampilkan Grafik ===#
Judul = ("\n Grafik Pendekatan Persamaan Differensial Biasa Dengan Metode Euler \n\n %s_%s_%s \n" % (Nama,NIM,Kelas))
plt.figure(figsize = (10, 8))
plt.plot(x, y, 'b:', label='Hasil Pendekatan')
plt.plot(x, G, '-g', label='Hasil Analitik')
plt.title(Judul) # Judul plot
plt.xlabel('x') # Label sumbu x
plt.ylabel('F(x)') # Label sumbu y
plt.grid() # Menampilkan grid
plt.legend(loc='lower right')
plt.show()

#METODE HEUN (MODUL 5)
print("Nama : Pramesthi Dwi Octavianna \n",
     "NIM : 6050119130086 \n",
     "Kelas : Oseanografi B \n")

#=== Import Library ===#
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
get_ipython().run_line_magic('matplotlib', 'inline')

#==== Mendefinisikan parameter dan fungsi ===#
h = float(input("Masukkan nilai h: ")) # Step size
x0 = float(input("Masukkan nilai x awal: "))
xn = float(input("Masukkan nilai x akhir: "))
x = np.arange(x0, xn + h, h) # Numerical grid
y0 = float(input("Masukkan nilai y awal: ")) # Initial Condition
G = 2*((x**3)) + 9*(x**2) + 3*(x) + 86
f = lambda x, y: 2*((x**3)) + 9*(x**2) + 3*(x) + 86 # Persamaan Differensial Biasa

#=== Metode Heun / Runge Kutta Orde 2 ===#
y = np.zeros(len(x))

y[0] = y0
for i in range(0, len(x) - 1):
    k1 = f(x[i], y[i])
    k2 = f((x[i]+h), (y[i]+(h*k1)))
    
    y[i+1] = y[i]+(0.5*h*(k1+k2))

print(y)
    
#=== Menghitung Error ===#
Galat = G-y
print (Galat)

#=== Menampilkan Grafik ===#
Judul = ("\n Grafik Pendekatan Persamaan Differensial Biasa Dengan Metode Heun \n\n %s_%s_%s \n" % (Nama,NIM,Kelas))
plt.figure(figsize = (8, 8))
plt.plot(x, y, 'b--', label='Hasil Pendekatan')
plt.plot(x, G, '-g', label='Hasil Analitik')
plt.title(Judul) # Judul plot
plt.xlabel('x') # Label sumbu x
plt.ylabel('F(x)') # Label sumbu y
plt.grid() # Menampilkan grid
plt.legend(loc='lower right')
plt.show()

