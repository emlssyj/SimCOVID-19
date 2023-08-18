using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AgentInfo : MonoBehaviour
{
    public string sex = "male";
    public int indicatorColor = 0;
    public int age = 14;
    public bool isMasked = false; // 是否戴口罩
    public float restDay = 0.0f; //当前阶段剩余天数
    public int vaccine = 0; //是否接种疫苗
    public int isolation = 0;
    public GameObject[] activityList;
    public GameObject[] relationshipList;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
