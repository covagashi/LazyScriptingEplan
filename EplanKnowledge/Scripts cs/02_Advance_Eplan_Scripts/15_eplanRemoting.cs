using Eplan.EplApi.RemoteClient;
using Eplan.EplApi.Starter;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace EPLAN_Remote_Client
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<EplanServerData> instancesActive = GetActiveEplanInstances();
            if (instancesActive.Any())
            {
                Console.WriteLine("Iniciar instancia activa...");
                EplanServerData eplanInstanceActive = instancesActive
                  .OrderBy(obj => obj.EplanVersion)
                  .Last();

                ExecuteActive(eplanInstanceActive);
            }
            else
            {
                Console.WriteLine("No se encontró ninguna instancia activa.");

                List<EplanData> instancesInstalled = GetInstalledEplanInstances();
                instancesInstalled = instancesInstalled
                  .Where(obj =>
                    obj.EplanVariant.Equals("Electric P8") &&
                    obj.EplanVersion.StartsWith("2023"))
                  .OrderBy(obj => obj.EplanVersion)
                  .ToList();
                if (instancesInstalled.Any())
                {
                    Console.WriteLine("Iniciar instancia instalada...");
                    EplanData eplanInstanceInstalled = instancesInstalled.Last();

                    ExecuteInstalled(eplanInstanceInstalled);
                }
                else
                {
                    Console.WriteLine("No se encontró ninguna instancia instalada.");
                }
            }

            Console.WriteLine("Ejecución completada.");
            Console.ReadKey();
        }

        public static List<EplanServerData> GetActiveEplanInstances()
        {
            EplanRemoteClient eplanRemoteClient = new EplanRemoteClient();
            List<EplanServerData> eplanServerDatas = new List<EplanServerData>();
            eplanRemoteClient.GetActiveEplanServersOnLocalMachine(
              out eplanServerDatas);
            return eplanServerDatas;
        }

        private static void ExecuteActive(EplanServerData eplanServerData)
        {
            EplanRemoteClient eplanRemoteClient = new EplanRemoteClient();
            eplanRemoteClient.SynchronousMode = true;
            eplanRemoteClient.Connect("localhost",
              eplanServerData.ServerPort.ToString(),
              new TimeSpan(0, 0, 0, 5)); // 5s needed to resolve

            eplanRemoteClient.ExecuteAction("Actionname");
            eplanRemoteClient.Disconnect();
            eplanRemoteClient.Dispose();
        }

        public static List<EplanData> GetInstalledEplanInstances()
        {
            EplanFinder eplanFinder = new EplanFinder();
            List<EplanData> eplanVersions = new List<EplanData>();
            eplanFinder.GetInstalledEplanVersions(ref eplanVersions, true);
            return eplanVersions;
        }

        private static void ExecuteInstalled(EplanData eplanData)
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = eplanData.EplanPath;

            const string QUOTE = "\"";
            string arguments = string.Format("/Variant:{0}{1}{0} {2}",
              QUOTE, eplanData.EplanVariant, "Actionname");

            startInfo.Arguments = arguments;
            Process.Start(startInfo);
        }
    }
}