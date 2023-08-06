# klarify

Easy but extendable command line interface for splitting large, multi-part .yaml files for kubernetes configuration into more easily managed and readable chunks, tied together with kustomization files.

Quick notes:

```
helm template aws-cloudwatch-metrics --namespace amazon-cloudwatch eks/aws-cloudwatch-metrics --set clusterName=my-eks-cluster > amazon-cloudwatch.yaml
```

Above command generates the amazon-cloudwatch.yaml file in the tests folder. Actual tests coming in future releases, along with documentation. I just wanted to get this initial working version available.
