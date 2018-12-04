using System;
using System.Linq;

namespace Puzzle2
{
    public class guard
    {
        public string ID { get; set; }
        public int totalSleep { get; set; }
        public int[] minutes { get; set; }
        public int commonMin { get; set; }
        public int commonMinTotal { get; set; }

        public guard(string g)
        {
            ID = g;
            totalSleep = 0;
            minutes = new int[60];
        }

        public void printInfo()
        {
            findCommon();
            Console.WriteLine("ID: " + ID + "\nTotal minutes: " + totalSleep + "\nCommon Minute: " + commonMin);
        }

        public void findCommon()
        {
            for (var x = 0; x < 60; x++)
            {
                if (minutes[x] > commonMin) { commonMin = minutes[x]; }
            }

            commonMin = Array.IndexOf(minutes, commonMin);
        }

        public void updateInfo() {
            commonMinTotal = minutes.Max();
            commonMin = Array.IndexOf(minutes, commonMinTotal);
        }
    }
}
