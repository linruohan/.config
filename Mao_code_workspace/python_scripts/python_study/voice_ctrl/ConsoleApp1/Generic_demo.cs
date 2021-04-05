using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    //泛型类型   示例
    class Generic_demo
    {
        static void Main(string[] args)
        {

            var dm = new DocumentManager<Document>();
            dm.AddDocument(new Document("Title A", "Content A"));
            dm.AddDocument(new Document("Title B", "Content B"));
            dm.DisplayAllDocuments();
            if (dm.IsDocumentAvailable)
            {
                Document doc = dm.GetDocument();
                Console.WriteLine(doc.Content);
            }


        }

        //泛型 类  文档管理器  
        public class DocumentManager<TDocument>
            where TDocument: IDocument//泛型约束：TDocument必须实现IDocument接口
        {
            //文档队列
            private readonly Queue<TDocument> documentQueue = new Queue<TDocument>();
            //添加文档到队列中
            public void AddDocument(TDocument doc)
            {
                lock (this)
                {
                    documentQueue.Enqueue(doc);
                }
            }
            public bool IsDocumentAvailable
            {
                get { return documentQueue.Count > 0; }
            }

            //获取文档
            public TDocument GetDocument()
            {
                TDocument doc = default(TDocument);//default关键字，将null赋予引用类型，将0赋予值类型
                lock (this)
                {
                    doc = documentQueue.Dequeue();
                }
                return doc;
            }
            //显示所有文档
            public void DisplayAllDocuments()
            {
                foreach (TDocument doc in documentQueue)
                {
                    Console.WriteLine(doc.Title);
                }
            }

        }
        //文档接口
        public interface IDocument
        {
            string Title { get; set; }
            string Content { get; set; }

        }
        public class Document : IDocument
        {
            public Document() { }

            public Document(string title, string content)
            {
                this.Title = title;
                this.Content = content;
            }

            public string Title { get ; set ; }
            public string Content { get; set; }


        }
    }
}
