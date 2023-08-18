using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class RedAIControl : MonoBehaviour
{
    // Start is called before the first frame update

    public GameObject seat;
    public float schoolTime = 10.0f; // �Ͽ�ʱ�䣬��λ����
    public float breakTime = 5.0f; // �¿�ʱ�䣬��λ����
    public int order;
    public Vector3 startPoint;
    public AgentManager agentManager;

    private int classcount = 1;
    private float timer = 0f;
    private float Alltimer = 0f;
    private int weekDay = 1;
    private bool isNoonTime = false;
    private bool isHomeTime = true;
    private bool isSchoolTime = true;
    public GameObject desk; // ��̨�ص�
    NavMeshAgent agent;

    private float infectionTimer = 0f;

    public GameObject indicator; // Բ��ɫ�����
    public SpriteRenderer indicatorRenderer; // Բ��ɫ��� Sprite Renderer ���
    public Color[] colors = { Color.white, Color.yellow, Color.red };
    float indicatorScale = 0.7f;
    void Start()
    {
        startPoint = transform.position;
        agent = GetComponent<NavMeshAgent>();
        agentManager = FindObjectOfType<AgentManager>();
        agentManager.AddAgent(agent);
        if (classcount == order)
        {
            GoToTeach();
        }
        else
        {
            GoToSeat();
        }
        
        StartCoroutine(ManageTime());

        indicator = new GameObject("Indicator");
        indicator.transform.parent = this.transform;
        indicator.transform.localPosition = Vector3.up * 2f; // ����λ����ͷ���Ϸ�
        indicator.transform.localScale = Vector3.one * indicatorScale;

        // ��� Sprite Renderer ����������ó�ʼ��ɫ
        indicatorRenderer = indicator.AddComponent<SpriteRenderer>();
        indicatorRenderer.sprite = CreateCircleSprite();

        indicatorRenderer.color = colors[GetComponent<AgentInfo>().indicatorColor];
    }
    // Update is called once per frame
    void Update()
    {

        //indicatorRenderer.color = isChilling ? Color.green : Color.white;
        if (Camera.main != null)
        {
            indicator.transform.LookAt(Camera.main.transform);

        }
        // ÿ���ж��Ƿ��Ⱦ
        infectionTimer += Time.deltaTime;
        if (infectionTimer >= 1f)
        {
            CheckInfection();
            infectionTimer = 0f; // ���ü�ʱ��
        }
    }
    private void GoToSeat()
    {
        // ʹ��NavMeshAgent�ƶ�����λ��λ��
        agent.SetDestination(seat.transform.position);
       // GetComponent<AgentInfo>().isMasked = false;
    }
    private void GoHome()
    {
        // ʹ��NavMeshAgent�ƶ�����λ��λ��
        agent.SetDestination(startPoint);
    }
    private void GoToTeach()
    {
        // ʹ��NavMeshAgent�ƶ�����λ��λ��
        agent.SetDestination(desk.transform.position);
        //GetComponent<AgentInfo>().isMasked = false;
    }

    private IEnumerator ManageTime()
    {
        while (true)
        {
            timer += Time.deltaTime;
            //Debug.Log(timer);
            Alltimer += Time.deltaTime;
             //Debug.Log(classcount);
            if (Alltimer < 110f)
            {
                if (isHomeTime)
                {
                    if (classcount % 4 == order)
                    {
                        GoToTeach();
                    }
                    else
                    {
                        GoToSeat();
                    }
                    isSchoolTime = true;
                    isHomeTime = false;
                }
                if (isSchoolTime)
                {
                    //timer += Time.deltaTime;
                    // Debug.Log(schoolTime);
                    if (timer >= schoolTime)
                    {
                        // �¿�ʱ��
                        GoToSeat();
                        isSchoolTime = false;
                        classcount++;
                        timer = 0f;
                    }
                    else
                    {
                        isSchoolTime = true;
                    }
                }
                else
                {
                    // timer += Time.deltaTime;
                    if (timer >= breakTime)
                    {
                        // �Ͽ�ʱ��
                        if(classcount % 4== order)
                        {
                            GoToTeach();   
                        }
                        isSchoolTime = true;
                        timer = 0f;

                    }
                }
            }
            else if (Alltimer > 110f && Alltimer < 150f)
            {
                if (isSchoolTime)
                {
                    GoHome();
                    isSchoolTime = false;
                    isNoonTime = true;

                }

            }
            else if (Alltimer >= 150f && Alltimer < 260f)
            {
                if (isNoonTime)
                {
                    if (classcount % 4 == order)
                    {
                        GoToTeach();
                    }
                    else
                    {
                        GoToSeat();
                    }
                    isSchoolTime = true;
                    isNoonTime = false;
                    timer = 0f;
                }
                if (isSchoolTime)
                {
                    //timer += Time.deltaTime;
                    // Debug.Log(schoolTime);
                    if (timer >= schoolTime)
                    {
                        // �¿�ʱ��
                        GoToSeat();
                        isSchoolTime = false;
                        classcount++;
                        timer = 0f;
                    }
                    else
                    {
                        isSchoolTime = true;
                    }
                }
                else
                {
                    // timer += Time.deltaTime;
                    if (timer >= breakTime)
                    {
                        // �Ͽ�ʱ��
                        if (classcount % 4 == order)
                        {
                            GoToTeach();
                        }
                        isSchoolTime = true;
                        timer = 0f;

                    }
                }
            }
            else if (Alltimer >= 260f && Alltimer < 270f)
            {
                if (isSchoolTime)
                {
                    GoHome();
                    isSchoolTime = false;
                    isHomeTime = true;
                    
                }

            }
            else
            {
                Alltimer = 0f;
                timer = 0f;

                UpdateInfectionSituation();
                if (GetComponent<AgentInfo>().isolation == 1)
                {
                    if (weekDay == 1)
                    {
                        if (GetComponent<AgentInfo>().indicatorColor == 2 || GetComponent<AgentInfo>().indicatorColor == 3)
                        {
                            GetComponent<AgentInfo>().restDay = 1;
                        }
                    }
                }
                else if (GetComponent<AgentInfo>().isolation == 2)
                {
                    if (GetComponent<AgentInfo>().indicatorColor == 2 || GetComponent<AgentInfo>().indicatorColor == 3)
                    {
                        GetComponent<AgentInfo>().restDay = 1;
                    }
                }
                if (weekDay < 5)
                {
                    weekDay++;
                }
                else
                {
                    weekDay = 1;
                }
            }

            yield return null;
        }
    }
    Sprite CreateCircleSprite()
    {
        int resolution = 64;
        Texture2D texture = new Texture2D(resolution, resolution);
        for (int i = 0; i < resolution; i++)
        {
            for (int j = 0; j < resolution; j++)
            {
                Color color = (Vector2.Distance(new Vector2(i, j), new Vector2(resolution / 2, resolution / 2)) < resolution / 2) ? Color.white : Color.clear;
                texture.SetPixel(i, j, color);
            }
        }
        texture.Apply();

        return Sprite.Create(texture, new Rect(0, 0, resolution, resolution), new Vector2(0.5f, 0.5f), resolution);
    }
    float GenerateWeibullRandom(float shape, float scale)
    {
        float u = Random.value; // Uniform random value between 0 and 1
        float x = scale * Mathf.Pow(-Mathf.Log(1.0f - u), 1.0f / shape);
        return x;
    }
    void CheckInfection()
    {
        Collider[] nearbyColliders = Physics.OverlapSphere(transform.position, 1.5f);
        foreach (var collider in nearbyColliders)
        {
            if (collider.CompareTag("Agent"))
            {
                AIControl nearbyAgent = collider.GetComponent<AIControl>();
                AgentInfo nearbyAgentInfo = collider.GetComponent<AgentInfo>();
                if (nearbyAgentInfo != null && (nearbyAgentInfo.indicatorColor == 2 || nearbyAgentInfo.indicatorColor == 3) && Random.Range(0f, 1f) <= ComputeInfectionChance(nearbyAgentInfo, GetComponent<AgentInfo>()))
                {
                    // �� 20% ���ʱ���Ⱦ��ͷ�ϵ� indicator ��Ϊ��ɫ
                    if (GetComponent<AgentInfo>().indicatorColor == 0)
                    {
                        indicatorRenderer.color = colors[1];
                        GetComponent<AgentInfo>().indicatorColor = 1;
                         GetComponent<AgentInfo>().restDay = GenerateWeibullRandom(1.9f, 5.0f);
                    }

                    break;
                }
            }
        }
    }
    float ComputeInfectionChance(AgentInfo nearbyAgentInfo, AgentInfo currentAgentInfo)
    {
        float infectiousness = 0.02f;

        if (nearbyAgentInfo.isMasked)
        {
            infectiousness *= 0.5f;
        }
        if (currentAgentInfo.isMasked)
        {
            infectiousness *= 0.7f;
        }
        if (currentAgentInfo.vaccine == 1)
        {
            infectiousness *= 0.48f;
        }
        if (currentAgentInfo.vaccine == 2)
        {
            infectiousness *= 0.054f;
        }
        if (currentAgentInfo.age < 18)
        {
            infectiousness *= (1.0f + (currentAgentInfo.age - 18) * 0.02f);
        }
        if (nearbyAgentInfo.indicatorColor == 2)
        {
            infectiousness *= 0.6f;
        }
        return infectiousness;
    }
    void UpdateInfectionSituation()
    {
        GetComponent<AgentInfo>().restDay -= 1.0f;
        if (GetComponent<AgentInfo>().restDay <= 0.0f)
        {
            if (GetComponent<AgentInfo>().indicatorColor == 1)
            {
                float symptomProbability = 0.85f;
                if (GetComponent<AgentInfo>().age < 18)
                {
                    symptomProbability *= (1.0f + (GetComponent<AgentInfo>().age - 18) * 0.025f);
                }
                if (Random.Range(0f, 1f) <= symptomProbability)
                {
                    GetComponent<AgentInfo>().indicatorColor = 2;
                    indicatorRenderer.color = colors[2];
                }
                else
                {
                    GetComponent<AgentInfo>().indicatorColor = 3;
                    indicatorRenderer.color = colors[3];
                }

                GetComponent<AgentInfo>().restDay = GenerateWeibullRandom(3.95f, 10.91f);
            }
            else if (GetComponent<AgentInfo>().indicatorColor == 2 || GetComponent<AgentInfo>().indicatorColor == 3)
            {
                GetComponent<AgentInfo>().indicatorColor = 4;
                indicatorRenderer.color = colors[4];
            }

        }
    }
}
