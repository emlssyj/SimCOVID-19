using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.AI;
using System;
using System.IO;

public class AgentStatic : MonoBehaviour
{
    public TMP_Text agentStaticText;
    public int agentCount = 0;
    public int uninfectedCount = 0;
    public int infectedCount = 0;
    public int incubationCount = 0;
    public int asymptomaticCount = 0;
    public int symptomaticCount = 0;
    public int immuneCount = 0;


    private const float realSecondToGameMinute = 2.0f;
    private float gameMinutes = 0.0f;
    private int days = 0;

    private StreamWriter writer;
    private string fileName;

    // Start is called before the first frame update
    void Start()
    {
        agentStaticText = GetComponent<TMP_Text>();
        string timestamp = DateTime.Now.ToString("yyyyMMddHHmmss");
        fileName = "DynamicCoordinates_" + timestamp + ".csv";
        Debug.Log(Application.dataPath + "/" + fileName);
        // Create or open the CSV file
        writer = new StreamWriter(Application.dataPath + "/" + fileName);
        writer.WriteLine("days" + "," + "uninfectedCount" + "," + "incubationCount" + "," + "asymptomaticCount" + "," + "symptomaticCount" + "," + "immuneCount");
    }

    // Update is called once per frame
    void Update()
    {
        agentCount = 0;
        uninfectedCount = 0;
        infectedCount = 0;
        incubationCount = 0;
        asymptomaticCount = 0;
        symptomaticCount = 0;
        immuneCount = 0;

        foreach (NavMeshAgent agent in GetComponent<AgentManager>().agents)
        {
            agentCount++;
            switch (agent.GetComponent<AgentInfo>().indicatorColor)
            {
                case 0:
                    uninfectedCount++;
                    break;
                case 1:
                    incubationCount++;
                    break;
                case 2:
                    asymptomaticCount++;
                    break;
                case 3:
                    symptomaticCount++;
                    break;
                case 4:
                    immuneCount++;
                    break;
                default:
                    break;
            }

        }
        agentStaticText.text = string.Format("Agents:{0:0} Uninfected:{1:0} Incubation:{2:0} Asymptomatic:{3:0} Symptomatic:{4:0} Immune:{5:0}", agentCount, uninfectedCount, incubationCount, asymptomaticCount, symptomaticCount, immuneCount);

        // 获取现实时间经过的秒数
        float realSecondsPassed = Time.deltaTime;

        // 将现实时间的秒数映射为游戏内时间的分钟
        gameMinutes += realSecondsPassed * realSecondToGameMinute;

        if (gameMinutes >= 540.0f)
        {
            gameMinutes = 0.0f;
            days++;
            //if(immuneCount == agentCount)
            //{
            //    Application.Quit();
            //}
            if(days<35)
            writer.WriteLine(days.ToString() + "," + uninfectedCount.ToString() + "," + incubationCount.ToString() + "," + asymptomaticCount.ToString() + "," + symptomaticCount.ToString() + "," + immuneCount.ToString());
            //Debug.Log(string.Format("Agents:{0:0} Uninfected:{1:0} Incubation:{2:0} Asymptomatic:{3:0} Symptomatic:{4:0} Immune:{5:0} Days:{6:0}", agentCount, uninfectedCount, incubationCount, asymptomaticCount, symptomaticCount, immuneCount, days));
        }
    }
    void OnDestroy()
    {
        // Close the writer when the script is destroyed
        if (writer != null)
        {
            writer.Close();
        }
    }
}
