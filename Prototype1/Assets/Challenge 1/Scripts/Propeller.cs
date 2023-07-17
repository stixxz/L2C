using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class Propeller : MonoBehaviour
{
    public Vector3 prop = new Vector3 (0,0,10);

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(prop);
    }
}
