**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

I've chosen to deploy all applications with replica count to 1, it's enough for the general representation of functionality. When I've tried to deploy per 3 replicas I noticed the excessive CPU consumption by the k3s server itself (not by pods).

![kubectl-get-all-monitoring](/answer-img/kubectl-get-all-monitoring.png)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![grafana-prom-jaeger-datasource-added](/answer-img/grafana-prom-jaeger-datasource-added.png)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![basic-dashboard-prometheus-as-ds](/answer-img/basic-dashboard-prometheus-as-ds.png)



## Describe SLO/SLI

*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

SLI ***monthly uptime*** : *monthly uptime* percentage of website/network application/physical server/etc.  is 99.8%. This is the ratio of percentage to the time during which website/network application/physical server/etc. is able to serve requests or perform programmed operations.

We can set our SLO goal for the future - ***monthly uptime*** percentage of website/network application/physical server/etc. to be 99.9%.

SLI ***request response time***- *request response time* of specified website/network application is 20 ms. This is the time during which the response is being handled by a remote website/network application.

We can set our SLO: ***request response time*** of website to 10 ms.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

The 4 of them we already know about and the 5th one is also popular metric - Uptime:

1. **Latency** - response time during which the requests are served, usually measured in milliseconds;
2. **Traffic** - the value of load on the target, usually measured in requests per second, or megabits/kilobits per second;
3. **Errors** - the amount of failed requests, usually measured in number of requests with return HTTP-code 500 in a second; 
4. **Saturation/Utilization** - indicates the percentage of system resources used (CPU usage %, Memory usage %/GB/MB);
5. **Uptime** -  the overall availability metric, could be shown as time from the last reboot/fail or more often as a percentage, indicating the ratio of time the monitored target was available for service to the time it wasn't (eg. 99.9% of uptime, so in contrast - 0.1% of overall time it was in downtime or in maintenance, it didn't serve its designated work).



## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![dashboard_to_measure_slis_1](/answer-img/dashboard_to_measure_slis_1.png)

![dashboard_to_measure_slis_2](/answer-img/dashboard_to_measure_slis_2.png)



## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

###### Python code for tracing in backend application:

![tracing_backend_trace_code](/answer-img/tracing_backend_trace_code.png)'

###### Let's perform a load to our backend API endpoints:

![tracing_backend_load_to_trace](/answer-img/tracing_backend_load_to_trace.png)

![tracing_backend_load_to_trace-2](/answer-img/tracing_backend_load_to_trace-2.png)

![tracing_backend_load_to_trace-3](/answer-img/tracing_backend_load_to_trace-3.png)

Actually this is too low load, I invoked then the series of:

`seq 1 1000 | xargs -Iname -P 100 curl localhost:8081`
`seq 1 1000 | xargs -Iname -P 100 curl localhost:8081/api`
`seq 1 300 | xargs -Iname -P 50 curl localhost:8081/nothing`
`seq 1 300 | xargs -Iname -P 50 curl localhost:8081/star`
`seq 1 100 | xargs -Iname -P 25 curl -d '{"name":"Sirius", "distance":"8.6"}' -H 'Content-Type: application/json' -X POST localhost:8081/star`
`seq 1 300 | xargs -Iname -P 50 curl localhost:8080/blablastuff`

-, trying to play around with amount of sequence for parallel crawling the endpoints.



###### Let's watch the traces in Jaeger UI:

![tracing_backend_jaeger-search](/answer-img/tracing_backend_jaeger-search.png)

###### And finally every trace is reflected in Grafana, too:

![tracing_backend_grafana_screenshot](/answer-img/tracing_backend_grafana_screenshot.png)



## Jaeger in Dashboards

*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![dashboard_jaeger_row](/answer-img/dashboard_jaeger_row.png)

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Backend Service Outage Suspected

Date: 11/25/2021 03:04:32

Subject: HTTP 500 Errors

Affected Area:  ''/star' API-endpoint of 'backend' service

Severity: Critical

Description: Got monitoring observations indicating that rising amount of HTTP 500 Errors at backend's '/star' endpoint with with a noticeable delays ~30 sec.


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

As our application I would consider 'backend-app' application:

1. **Uptime**. <u>SLI</u>: Uptime of the application availability per month. <u>SLO</u>: Uptime of the application - 99.95%.
2. **Latency**:
   - <u>SLI</u>: Average response time per 30 seconds periods per month. <u>SLO</u>: Average response time per 30 sec periods per month less than 100ms. 
   - <u>SLI</u>: Percentage of request count which complete in less than 100ms. <u>SLO</u>: 99% of request count will complete in less than 100ms.
3. **Errors**. <u>SLI:</u> HTTP 500 errors % rate per 1 minute ranges. <u>SLO</u>:  HTTP 500 errors % rate per 1 minute is less than 1%.
4. **Traffic**. <u>SLI</u>: Total requests per minute. <u>SLO</u>: Total requests per minute is less than 1800.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

1. Uptime of the application availability per month (this is an embracing SLI indicating overall availability of our application).
2. Average response time per 30 sec periods per month less than 100ms (this would indicate that the application smoothly serves the requests, bearing the load). 
3. HTTP 500 errors % rate per 1 minute ranges (small amount of errors is acceptable, and vice versa - rising amount of errors HTTP500 is a good sign for examination of possible issues in the application and infrastructure in general).

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

Dashboard: General / Udacity CNDA Dashboards Project:

Row 'Prometheus':

- <u>CPU Usage</u>: CPU Usage fractions of 2 application deployments - backend-app and frontend-app;
- <u>Memory Usage</u>: Memory usage in MiB of 2 application deployments - backend-app and frontend-app;
- <u>Uptime ('frontend')</u>: frontend application uptime graph;
- <u>Uptime ('backend')</u>: backend application uptime graph;
- <u>HTTP 4xx Errors</u>: the number of HTTP requests with response code 4xx, over 30 sec intervals, shown per application and path;
- <u>HTTP 5xx Errors</u>: the number of HTTP requests with response code 5xx, over 30 sec intervals, shown per application and path;
- <u>HTTP requests per second</u>: the number of HTTP requests per second;
- <u>Total requests per minute</u>: the amount of all HTTP requests measured over one minute intervals;
- <u>Average response time [30s]</u>: the average response time for HTTP requests over 30 sec intervals, shown per application and path;
- <u>Requests under 100ms</u>: the percentage of requests which were finished within 100ms, shown per application and path;
- <u>HTTP 5xx Errors % rate per minute</u>: the percentage rate of HTTP 5xx errors per 1 minute intervals;

Row 'Jaeger':

- <u>Min latency ( backend '/api' )</u>: minimal latency in milliseconds of the requests which were served by the '/api' endpoint of backend app, within the specified time range;
- <u>Avg latency ( backend '/api' )</u>: average latency in milliseconds of the requests which were served by the '/api' endpoint of backend app, within the specified time range;
- <u>Max latency ( backend '/api' )</u>: maximum latency in milliseconds of the requests which were served by the '/api' endpoint of backend app, within the specified time range;
- <u>Requests Count by Latency ( backend '/api' )</u>: the amount of total requests served by the backend 'api'-endpoint distributed by the serving duration, within the specified time range;
- <u>Backend HTTP 500 Errors Count Indicator</u>: the amount of requests with response code HTTP 500, served by the backend 'api'-endpoint distributed by the serving duration, within the specified time range.

![final-dashboard1](/answer-img/final-dashboard1.png)

![final-dashboard2](/answer-img/final-dashboard2.png)

![final-dashboard3](/answer-img/final-dashboard3.png)



Dashboard: General / Udacity CNDA Dashboards Project / KPI:

- <u>Uptime ('backend')</u>: backend application uptime graph;
- <u>Average response time [30s]</u>: the average response time for HTTP requests over 30 sec intervals, shown per application and path;
- <u>HTTP 5xx Errors % rate per minute</u>: the percentage rate of HTTP 5xx errors per 1 minute intervals;![dashboard_kpis](/answer-img/final-dashboard-kpi.png)
