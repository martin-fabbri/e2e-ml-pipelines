# Automating End-to-End Machine Learning Pipelines

This repository explores different approaches to automate end-to-end machine learning workflows. One of our goals is to leverage the existing principles and practices of Continous Delivery to machine learning uses cases.

Machine learning is progressively taking a central role in developing solutions. However, the process for developing, deploying, and continuously improving them is more complex compared to more traditional software, such as a web service or a mobile application. They are subject to change in three axes: the code itself, the model, and the data. Their behavior is often complex and hard to predict, and they are harder to test, harder to explain, and harder to improve.

The three axes mentioned above: **code** + **model** + **data** should be treated as one immutable entity. Any change to this entity should be versioned making possible to share experiments at different stages. It should suffice to unpack any of these entities and rerun the experiment to reproduce the results obtained at any point in time.

By encapsulating our entities in containers, we enable sharing resources on multi-tenant environments. Each task should run independently using its own provisioned dependencies. This level of isolation it's one of Kubernetes' features, making this system very appealing for this kind of workflows.

## Recipes

* TODO: Add a recipe describing how to extract Jupyter code and automatically generate deployable tasks.

| Platform | Maintainer |
|------|------|
| Flyte | Lyft |
| Railyard | Stripe |
| Bighead | Airbnb |
| TFX | Google |



