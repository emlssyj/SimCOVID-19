using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.AI;

public class AgentManager : MonoBehaviour
{
    public List<NavMeshAgent> agents = new List<NavMeshAgent>();

    // 添加代理到列表
    public void AddAgent(NavMeshAgent agent)
    {
        agents.Add(agent);
    }

    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
