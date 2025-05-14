<a href="URL" target="[https://github.com/JingGu-hub/NoiSFluc](https://anonymous.4open.science/r/NoiTFFR)"><h1>NoiTFFR: Robust Multivariate Time Series Classification with Noisy Labels via Time-Frequency Features and Fluctuation-Resistant</h1></a>
This repository is the official implementation of NoiTFFR: Robust Multivariate Time Series Classification with Noisy Labels via Time-Frequency Features and Fluctuation-Resistant.

<h2>Abstract</h2>
Noisy labels pose persistent and significant challenges in training robust neural networks. While extensive research has been conducted on addressing noisy labels, the specific challenges associated with time series data remain underexplored. Existing studies on noisy labels often overlook key characteristics of time series
data, such as time-frequency characteristics and data fluctuations. To bridge this gap, we propose NoiTFFR, a novel method designed to mitigate the impact of noisy labels in time series data. Specifically, NoiTFFR incorporates a noise-resistant, multi-scale time-frequency features extractor (TimeFrequencyBlock) that captures multivariate time series features while minimizing the influence of noisy labels. Additionally, a delayed cross-entropy (DCE) loss function is introduced, which selectively filters clean samples from noisy data to enhance classification model training. Furthermore, we propose ensemble label cumulation (EnLabelc), a sample relabeling technique that corrects noisy labels and reintegrates them into the training process. Experimental results demonstrate that NoiTFFR outperforms state-of-the-art methods by an average of 15\% across multiple benchmark time series datasets, underscoring its effectiveness and robustness.

<h2>Datasets</h2>
<h3>UEA 30 archive time series datasets</h3>

* <a href="https://www.timeseriesclassification.com/dataset.php" target="_blank">UEA 30 archive</a>

<h3>Two individual large time series datasets</h3>

* <a href="http://archive.ics.uci.edu/ml" target="_blank">HAR dataset</a>
* <a href="https://www.mustafabaydogan.com/research/time-series-data-mining/symbolic-representations-for-multivariate-time-series-classification-smts/" target="_blank">UWave dataset</a>

<h2>Running NoiSFluc on benchmark datasets</h2>
Here is an example:

```bash
python main.py --archive UEA --dataset ArticularyWordRecognition --noise_type symmetric --label_noise_rate 0.5
```

<h2>Citation</h2>
If you use this code for your research, please cite our paper:
