using System.Collections.Generic;

namespace CmdGame
{
    partial class Program
    {
        public class RenderInfos
        {
            public List<RenderInfo> infos = new List<RenderInfo>();
            public List<object> extraInfos = new List<object>();
            public void AddExtraInfo(object obj)
            {
                extraInfos.Add(obj);
            }
            public void AddExtraInfos<T>(IEnumerable<T> objs)
            {
                foreach (var item in objs)
                {
                    extraInfos.Add(item);
                }
            }

            public void AddInfo(RenderInfo info)
            {
                infos.Add(info);
            }
            public List<RenderInfo> GetInfos()
            {
                return infos;
            }
            public List<object> GetExtraInfos()
            {
                return extraInfos;
            }

        }


    }
}
