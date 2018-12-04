using System;
using System.Collections.Generic;

namespace Puzzle2
{
    public class shift
    {
        public Dictionary<string, string> actions { get; set; }
        public string Date { get; set; }
        public string guardOnDuty { get; set; }

        public shift(string d)
        {
            actions = new Dictionary<string, string>();
            Date = d;
        }

        public void printInfo()
        {
            string result = "";
            List<string> keys = new List<string>(actions.Keys);
            for (int w = 0; w < keys.Count; w++)
            {
                result += "Key: " + keys[w] + " Action: " + actions[keys[w]] + " ";
            }
            Console.WriteLine("Date: " + Date + "\nGuard on Duty: #" + guardOnDuty + "\nActions: " + result);
        }
    }
}
