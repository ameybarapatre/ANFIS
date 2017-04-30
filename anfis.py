import tensorflow as tf
import pandas as pd
import os
import pandas as pd
import numpy as np

def taxi_eligibility(taxi,taxis_y ,alpha ,Gamma):
    n_membership = 4
    y = tf.placeholder("float",[None , 3])
    x = tf.placeholder("float", [None, n_membership])
    reward = tf.placeholder("float" ,[None , 1])

    rule3 = x
    rule4 = y
    rule1, rule2 = tf.split(x,[2,2],1)

    w1 = tf.reduce_prod(rule1 , axis = 1,keep_dims=True)
    w2 = tf.reduce_prod(rule2 , axis = 1,keep_dims=True)
    w3 = tf.reduce_prod(rule3 , axis = 1,keep_dims=True)
    w4 = tf.reduce_prod(rule4 ,axis=1 , keep_dims=True)
    w =  tf.add_n([w1,w2,w3,w4])

    w_inputs = tf.concat([w1,w2,w3,w4] , axis =1)
    w_inputs_ = tf.div(w_inputs , w)

    z= tf.Variable(tf.random_normal([4,1]))


    Q = tf.matmul(w_inputs_,z)

    maxQ = tf.reduce_max(Q ,axis=0, keep_dims=True)

    maxQs =tf.matmul(tf.ones(tf.shape(Q)),maxQ)
    gamma = tf.constant([[Gamma]])
    eQ = tf.add( reward , tf.matmul( maxQs ,gamma) )

    loss =tf.pow(tf.subtract( eQ , Q),2)
    optimizer = tf.train.AdamOptimizer(learning_rate=alpha).minimize(loss)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    saver = tf.train.Saver()

    data = pd.read_csv("fuzzyq1.csv")
    taxis = data[["ua","ub","uc","ud"]].as_matrix()
    r = (data['Diff']*10).as_matrix()[:,np.newaxis]
    y_in = data[["ub","ud","ua"]].as_matrix()
    if os.path.exists("checkpoint")!=True:
        for i in range(0,10000):
           sess.run([optimizer ], feed_dict={x: taxis ,reward:r , y : y_in})

        save_path = saver.save(sess, "./")
    else :
        saver.restore(sess, "./")
        print("Restored")

    taxi_in = np.array(taxi)

    return sess.run(Q, feed_dict={x: taxi_in, y:taxis_y})

if __name__=="__main__" :
    E = taxi_eligibility([[0.4216668178867803,0.32799309442505115,0.7501831501831502,0.8334689890932769]])
    print(E ,"Done Here")