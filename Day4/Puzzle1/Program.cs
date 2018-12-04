using System;
using System.Collections.Generic;
using System.Linq;

namespace Puzzle1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\Butterstroke\Documents\GitHub\Advent-Of-Code-2018\Day4\input.txt");

            Dictionary<string, shift> shifts = new Dictionary<string, shift>();
            Dictionary<string, guard> guards = new Dictionary<string, guard>();
            int[] minutes = new int[60];
            guard topSleeper = null;

            for (int x = 0; x < lines.Length; x++)
            {
                string date = lines[x].Substring(6, 5);
                string hourTime = lines[x].Substring(12, 2);
                string minTime = lines[x].Substring(15, 2);
                var action = lines[x].Substring(19);

                //Starts the person on the next shift if they clock in early.
                if (hourTime == "23")
                {
                    int newDay = Convert.ToInt32(date.Substring(3, 2)) + 1;
                    string newVal;
                    if (newDay < 10) { newVal = "0" + newDay; }
                    else { newVal = Convert.ToString(newDay); }

                    date = date.Substring(0, 3) + newVal;
                }

                for (int y = 0; y < shifts.Count; y++)
                {
                    if (shifts.ContainsKey(date))
                    {
                        if (action.StartsWith("Guard"))
                        {
                            int end = action.IndexOf("b");
                            shifts[date].guardOnDuty = action.Substring(7, (end - 7));
                        }
                        else
                        {
                            if (!shifts[date].actions.ContainsKey(minTime)) {
                                shifts[date].actions.Add(minTime, action);
                            }
                        }
                    }
                    else if (y + 1 == shifts.Count)
                    {
                        shift tempShift = new shift(date);

                        if (action.StartsWith("Guard"))
                        {
                            int end = action.IndexOf("b");
                            tempShift.guardOnDuty = action.Substring(7, (end - 7));
                        }
                        else
                        {
                            tempShift.actions.Add(minTime, action);
                        }

                        shifts.Add(date, tempShift);
                    }
                }

                if (shifts.Count == 0)
                {
                    shift tempShift = new shift(date);

                    if (action.StartsWith("Guard"))
                    {
                        int end = action.IndexOf("b");
                        tempShift.guardOnDuty = action.Substring(7, (end - 7));
                    }
                    else
                    {
                        tempShift.actions.Add(minTime, action);
                    }

                    shifts.Add(date, tempShift);
                }
            }

            List<string> shiftKeys = new List<string>(shifts.Keys);

            for (int x = 0; x < shiftKeys.Count; x++)
            {
                if (shifts[shiftKeys[x]].guardOnDuty != null)
                {
                    if (guards.Count == 0)
                    {
                        guards.Add(shifts[shiftKeys[x]].guardOnDuty, new guard(shifts[shiftKeys[x]].guardOnDuty));
                    }
                    else
                    {
                        Boolean check = false;
                        for (int y = 0; y < guards.Count; y++)
                        {
                            if (guards.ContainsKey(shifts[shiftKeys[x]].guardOnDuty))
                            {
                                check = true;
                            }
                            if (check == false && guards.Count == y + 1)
                            {
                                guards.Add(shifts[shiftKeys[x]].guardOnDuty, new guard(shifts[shiftKeys[x]].guardOnDuty));
                            }
                        }
                    }
                }
            }

            guard onDuty = null;

            for (int x = 0; x < shifts.Count; x++)
            {
                try
                {
                    onDuty = guards[shifts[shiftKeys[x]].guardOnDuty];
                }
                catch {
                    onDuty = null;
                }

                int start = 0;
                int[] total = new int[10];
                int z = 0;

                if (onDuty != null)
                {
                    for (int y = 0; y < 60; y++)
                    {
                        string baka = null;
                        if (y < 10) { baka = "0" + y; }
                        else { baka = Convert.ToString(y); }

                        if (shifts[shiftKeys[x]].actions.ContainsKey(baka))
                        {
                            if (shifts[shiftKeys[x]].actions[baka].StartsWith("falls"))
                            {
                                start = y;
                            }
                            else
                            {
                                for (int a = start; a < y; a++)
                                {
                                    minutes[a] += 1;
                                    onDuty.minutes[a] += 1;
                                }

                                total[z] = y - start;
                                z++;
                            }
                        }
                    }

                    onDuty.totalSleep += total.Sum();

                    if (topSleeper == null || topSleeper.totalSleep < onDuty.totalSleep) { topSleeper = onDuty; }
                }

                onDuty = null;
            }

            topSleeper.printInfo();

            Console.WriteLine("Answer: " + (Convert.ToInt32(topSleeper.ID) * topSleeper.commonMin));
            Console.ReadLine();
        }
    }
}
