import concurrent.futures
# import multiprocessing
import pandas
import threading
import xml.etree.ElementTree
import time
import os
import collections
# import queue
import re



def get(file_path:str):#获取地址,多线程获取所有xml具体地址并存放
  inner = os.listdir(file_path)
  for file in inner:
    true_path = file_path + '/' + file
    if(os.path.isdir(true_path)):
      thread = threading.Thread(target=get,args=(true_path,))
      thread.start()
      thread_pool.append(thread)
    else:
      l.acquire()
      xml_list.append(true_path)
      l.release()



def read(path:str):#读取，按照存放的地址读取并提取单词存入总单词列表
  # l.acquire()
  words_list = []
  tree = xml.etree.ElementTree.parse(path)
  root = tree.getroot()
  for child in root.iter():
    if(child.text!=None):
      words = re.findall(r'\b\w+\b',child.text)
      if(words!=None):
        for i in words:
          words_list.append(i)
  return words_list      



def run(path):#线程池
  re = []
  ts = []
  t_pool = concurrent.futures.ThreadPoolExecutor()
  for i in path:
    t = t_pool.submit(read,i)
    ts.append(t)
  for k in ts:
    re = re + k.result()
  return re




if __name__ == '__main__':

  l = threading.Lock()

  t1 = time.time()
  xml_list = []
  thread_pool = []
  result =[]
  root_path = './Python/download'



  thread_pool.append(threading.Thread(target=get,args=(root_path,)))#获取地址
  thread_pool[0].start()
  for t in thread_pool:
    t.join()



  pool =concurrent.futures.ProcessPoolExecutor(max_workers=2)
  pro1 =pool.submit(run,xml_list[:len(xml_list)//2])
  pro2 = pool.submit(run,xml_list[len(xml_list)//2:])
  result = pro1.result() + pro2.result()



  counts = collections.Counter(result)
  df = pandas.DataFrame(list(counts.items()), columns=['Word', 'Count'])

  df.to_csv('word_counts.csv', index=False)



  t2 = time.time()
  print(t2-t1)