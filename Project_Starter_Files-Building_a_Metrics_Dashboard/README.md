**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

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

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

###### Python code for tracing in backend application:

![tracing_backend_trace_code](/answer-img/tracing_backend_trace_code.png)'

###### Let's perform a load to our backend API endpoints:

![tracing_backend_load_to_trace](/answer-img/tracing_backend_load_to_trace.png)

![tracing_backend_load_to_trace-2](/answer-img/tracing_backend_load_to_trace-2.png)

![tracing_backend_load_to_trace-3](/answer-img/tracing_backend_load_to_trace-3.png)



###### Let's watch the traces in Jaeger UI:

![tracing_backend_jaeger-search](/answer-img/tracing_backend_jaeger-search.png)

###### And finally every trace is reflected in Grafana, too:

![tracing_backend_grafana_screenshot](/answer-img/tracing_backend_grafana_screenshot.png)



## Jaeger in Dashboards

*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
