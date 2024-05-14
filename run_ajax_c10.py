from flask import Flask
import pandas as pd
#全局路由初始化
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar, Pie, Timeline, Tab, Grid, Sunburst, WordCloud, Map, Page, Liquid, Radar, Line, Funnel
from flask import Flask,render_template

app = Flask(__name__)

class GetData:
    def __init__(self):
        self.df = pd.read_csv('work_data.csv', encoding='utf-8')
        # df.shape
        self.df.drop_duplicates(inplace=True)
        self.df.fillna(0, inplace=True)
        self.huafeng = {'华东': ['上海', '江苏', '浙江', '安徽', '江西', '山东', '福建'],
                        '华北': ['北京', '天津', '山西', '河北', '内蒙古'],
                        '华中': ['河南', '湖北', '湖南'],
                        '华南': ['广东', '广西', '海南'],
                        '西南': ['重庆', '四川', '贵州', '云南', '西藏'],
                        '西北': ['陕西', '甘肃', '青海', '宁夏', '新疆'],
                        '东北': ['黑龙江', '吉林', '辽宁']
                        }

        def fun(x):
            x = x.replace('省', '')
            x = x.replace('维吾尔自治区', '')
            x = x.replace('自治区', '')
            x = x.replace('壮族', '')
            x = x.replace('回族', '')
            x = x.replace('市', '')
            return x

        def industry_fun(x):
            x = x.replace('农、林、牧、渔业城镇私营单位就业人员平均工资', '农林牧渔业城镇私营单位就业人员平均工资')
            x = x.replace('电力、燃气及水的生产和供应业城镇私营单位就业人员平均工资', '电力、热力、燃气及水生产和供应业城镇私营单位就业人员平均工资')
            x = x.replace('信息传输、计算机服务和软件业城镇私营单位就业人员平均工资', '信息传输、软件和信息技术服务业城镇私营单位就业人员平均工资')
            x = x.replace('科学研究、技术服务和地质勘查业城镇私营单位就业人员平均工资', '科学研究和技术服务业城镇私营单位就业人员平均工资')
            x = x.replace('居民服务和其他服务业城镇私营单位就业人员平均工资', '居民服务、修理和其他服务业城镇私营单位就业人员平均工资')
            x = x.replace('教育城镇私营单位就业人员平均工资', '教育业城镇私营单位就业人员平均工资')
            x = x.replace('卫生、社会保障和社会福利业城镇私营单位就业人员平均工资', '卫生和社会工作城镇私营单位就业人员平均工资')
            x = x.replace('公共管理和社会组织城镇私营单位就业人员平均工资', '文化、体育和娱乐业城镇私营单位就业人员平均工资')
            x = x.replace('农、林、牧、渔业城镇单位就业人员平均工资', '农林牧渔业城镇单位就业人员平均工资')
            x = x.replace('电力、燃气及水的生产和供应业城镇单位就业人员平均工资', '电力、热力、燃气及水生产和供应业城镇单位就业人员平均工资')
            x = x.replace('信息传输、计算机服务和软件业城镇单位就业人员平均工资', '信息传输、软件和信息技术服务业城镇单位就业人员平均工资')
            x = x.replace('科学研究、技术服务和地质勘查业城镇单位就业人员平均工资', '科学研究和技术服务业城镇单位就业人员平均工资')
            x = x.replace('居民服务和其他服务业城镇单位就业人员平均工资', '居民服务、修理和其他服务业城镇单位就业人员平均工资')
            x = x.replace('教育城镇单位就业人员平均工资', '教育业城镇单位就业人员平均工资')
            x = x.replace('卫生、社会保障和社会福利业城镇单位就业人员平均工资', '卫生和社会工作城镇单位就业人员平均工资')
            x = x.replace('公共管理和社会组织城镇单位就业人员平均工资', '公共管理、社会保障和社会组织城镇单位就业人员平均工资')
            return x

        self.df['city'] = self.df['city'].apply(lambda x: fun(x))
        self.df['industry'] = self.df['industry'].apply(lambda x: industry_fun(x))
        self.work_hangye_chengzhen = self.df.query('industry == "农林牧渔业城镇单位就业人员"or industry == "采矿业城镇单位就业人员" \
                                 or industry == "制造业城镇单位就业人员" or industry == "电力、热力、燃气及水生产和供应业城镇单位就业人员" \
                                 or industry == "建筑业城镇单位就业人员" or industry == "交通运输、仓储和邮政业城镇单位就业人员" \
                                 or industry == "信息传输、软件和信息技术服务业城镇单位就业人员" or industry == "批发和零售业城镇单位就业人员" \
                                 or industry == "住宿和餐饮业城镇单位就业人员" or industry == "金融业城镇单位就业人员" \
                                 or industry == "房地产业城镇单位就业人员" or industry == "租赁和商务服务业城镇单位就业人员"\
                                 or industry == "科学研究和技术服务业城镇单位就业人员" or industry == "水利、环境和公共设施管理业城镇单位就业人员" \
                                 or industry == "居民服务、修理和其他服务业城镇单位就业人员" or industry == "教育业城镇单位就业人员"\
                                 or industry == "卫生和社会工作城镇单位就业人员" or industry == "文化、体育和娱乐业城镇单位就业人员"\
                                 or industry == "公共管理、社会保障和社会组织城镇单位就业人员"')
        self.work_hangye_sige = self.df.query('industry == "制造业私营企业和个体就业人员" \
                                 or industry == "建筑业私营企业和个体就业人员" or industry == "交通运输、仓储和邮政业私营企业和个体就业人员"\
                                 or industry == "批发和零售业私营企业和个体就业人员" or industry == "住宿和餐饮业私营企业和个体就业人员"\
                                 or industry == "租赁和商务服务业私营企业和个体就业人员" or industry == "居民服务和其他服务业私营企业和个体就业人员"')
        self.work_hangye_chengzhen_sige = self.df.query('industry == "城镇私营企业和个体就业人员" or industry =="制造业城镇私营企业和个体就业人员"\
                                 or industry =="建筑业城镇私营企业和个体就业人员"or industry =="交通运输、仓储和邮政业城镇私营企业和个体就业人员"\
                                 or industry =="批发和零售业城镇私营企业和个体就业人员"or industry =="住宿和餐饮业城镇私营企业和个体就业人员"\
                                 or industry =="租赁和商务服务业城镇私营企业和个体就业人员"or industry =="居民服务和其他服务业城镇私营企业和个体就业人员"')
        self.work_siying = self.df.query('industry == "私营企业户数" or industry == "私营企业就业人数" or industry == "私营企业投资者就业人数" \
                                 or industry == "城镇私营企业就业人数" or industry == "城镇私营企业投资者就业人数" \
                                 or industry == "乡村私营企业就业人数" or industry == "乡村私营企业投资者就业人数"')
        self.work_geti = self.df.query(
            'industry == "个体户数" or industry == "个体就业人数" or industry == "城镇就业人数" or industry == "乡村个体就业人数"')
        self.wage_chengzhen_zong = self.df.query('industry == "城镇单位就业人员工资总额" or industry == "国有城镇单位就业人员工资总额"\
                                 or industry == "城镇集体单位就业人员工资总额" or industry == "其他城镇单位就业人员工资总额"\
                                 or industry == "城镇单位就业人员工资总额指数(上年=100)" or industry == "国有城镇单位就业人员工资总额指数(上年=100)" \
                                 or industry == "城镇集体单位就业人员工资总额指数(上年=100)" or industry == "其他城镇单位就业人员工资总额指数(上年=100)"')
        self.wage_chengzhen_pingjun = self.df.query('industry == "城镇单位就业人员平均工资" or industry == "城镇单位在岗职工平均工资" or industry == "城镇国有单位就业人员平均工资"\
                                 or industry == "城镇集体单位就业人员平均工资" or industry == "城镇其他单位就业人员平均工资" or industry == "城镇单位就业人员平均货币工资指数(上年=100)" \
                                 or industry == "城镇单位在岗职工平均货币工资指数(上年=100)" or industry == "国有城镇单位就业人员平均货币工资指数(上年=100)" or industry == "城镇集体单位就业人员平均货币工资指数(上年=100)"\
                                 or industry == "其他城镇单位就业人员平均货币工资指数(上年=100)" or industry == "城镇单位就业人员平均实际工资指数(上年=100)" or industry == "城镇单位在岗职工平均实际工资指数(上年=100)"\
                                 or industry == "国有城镇单位就业人员平均实际工资指数(上年=100)" or industry == "城镇集体单位就业人员平均实际工资指数(上年=100)" or industry == "其他城镇单位就业人员平均实际工资指数(上年=100)"')
        self.wage_zhuce_chengzhen_pingjun = self.df.query('industry == "城镇单位就业人员平均工资" or industry == "国有单位就业人员平均工资" or industry == "城镇集体单位就业人员平均工资" \
                                 or industry == "股份合作单位就业人员平均工资" or industry == "联营单位就业人员平均工资" or industry == "有限责任公司就业人员平均工资" \
                                 or industry == "股份有限公司就业人员平均工资" or industry == "其他单位就业人员平均工资" or industry == "港、澳、台商投资单位就业人员平均工资" \
                                 or industry == "外商投资单位就业人员平均工资"')
        self.wage_hangye_chengzhen_zong = self.df.query('industry == "农、林、牧、渔业城镇单位就业人员工资总额" or industry =="城镇单位就业人员工资总额" or industry == "采矿业城镇单位就业人员工资总额" \
                                 or industry == "制造业城镇单位就业人员工资总额" or industry == "电力、燃气及水的生产和供应业城镇单位就业人员工资总额" \
                                 or industry == "建筑业城镇单位就业人员工资总额" or industry == "交通运输、仓储和邮政业城镇单位就业人员工资总额" \
                                 or industry == "信息传输、计算机服务和软件业城镇单位就业人员工资总额" or industry == "批发和零售业城镇单位就业人员工资总额" \
                                 or industry == "住宿和餐饮业城镇单位就业人员工资总额" or industry == "金融业城镇单位就业人员工资总额" \
                                 or industry == "房地产业城镇单位就业人员工资总额" or industry == "租赁和商务服务业城镇单位就业人员工资总额"\
                                 or industry == "科学研究、技术服务和地质勘查业城镇单位就业人员工资总额" or industry == "水利、环境和公共设施管理业城镇单位就业人员工资总额" \
                                 or industry == "居民服务和其他服务业城镇单位就业人员工资总额" or industry == "教育城镇单位就业人员工资总额"\
                                 or industry == "卫生、社会保障和社会福利业城镇单位就业人员工资总额" or industry == "文化、体育和娱乐业城镇单位就业人员工资总额"\
                                 or industry == "公共管理和社会组织城镇单位就业人员工资总额"')
        self.wage_hangye_chengzhen_pingjun = self.df.query('industry == "农林牧渔业城镇单位就业人员平均工资"or industry == "采矿业城镇单位就业人员平均工资" \
                                 or industry == "制造业城镇单位就业人员平均工资" or industry == "电力、热力、燃气及水生产和供应业城镇单位就业人员平均工资" \
                                 or industry == "建筑业城镇单位就业人员平均工资" or industry == "交通运输、仓储和邮政业城镇单位就业人员平均工资" \
                                 or industry == "信息传输、软件和信息技术服务业城镇单位就业人员平均工资" or industry == "批发和零售业城镇单位就业人员平均工资" \
                                 or industry == "住宿和餐饮业城镇单位就业人员平均工资" or industry == "金融业城镇单位就业人员平均工资" \
                                 or industry == "房地产业城镇单位就业人员平均工资" or industry == "租赁和商务服务业城镇单位就业人员平均工资"\
                                 or industry == "科学研究和技术服务业城镇单位就业人员平均工资" or industry == "水利、环境和公共设施管理业城镇单位就业人员平均工资" \
                                 or industry == "居民服务、修理和其他服务业城镇单位就业人员平均工资" or industry == "教育业城镇单位就业人员平均工资"\
                                 or industry == "卫生和社会工作城镇单位就业人员平均工资" or industry == "文化、体育和娱乐业城镇单位就业人员平均工资"\
                                 or industry == "公共管理、社会保障和社会组织城镇单位就业人员平均工资"')
        self.wage_hangye_chengzhensiying_pingjun = self.df.query('industry == "农林牧渔业城镇私营单位就业人员平均工资"or industry == "采矿业城镇私营单位就业人员平均工资" \
                                 or industry == "制造业城镇私营单位就业人员平均工资" or industry == "电力、热力、燃气及水生产和供应业城镇私营单位就业人员平均工资" \
                                 or industry == "建筑业城镇私营单位就业人员平均工资" or industry == "交通运输、仓储和邮政业城镇私营单位就业人员平均工资" \
                                 or industry == "信息传输、软件和信息技术服务业城镇私营单位就业人员平均工资" or industry == "批发和零售业城镇私营单位就业人员平均工资" \
                                 or industry == "住宿和餐饮业城镇私营单位就业人员平均工资" or industry == "金融业城镇私营单位就业人员平均工资" \
                                 or industry == "房地产业城镇私营单位就业人员平均工资" or industry == "租赁和商务服务业城镇私营单位就业人员平均工资"\
                                 or industry == "科学研究和技术服务业城镇私营单位就业人员平均工资" or industry == "水利、环境和公共设施管理业城镇私营单位就业人员平均工资" \
                                 or industry == "居民服务、修理和其他服务业城镇私营单位就业人员平均工资" or industry == "教育业城镇私营单位就业人员平均工资"\
                                 or industry == "卫生和社会工作城镇私营单位就业人员平均工资" or industry == "文化、体育和娱乐业城镇私营单位就业人员平均工资"\
                                 or industry == "公共管理、社会保障和社会组织城镇私营单位就业人员平均工资"')
        self.shiye = self.df.query('industry == "城镇登记失业人数" or industry == "城镇登记失业率"')
        self.city = ['新疆', '宁夏', '青海', '甘肃', '陕西', '西藏', '云南', '贵州', '四川', '重庆', '海南', '广西', '广东'
            , '湖南', '湖北', '河南', '山东', '江西', '福建', '安徽', '浙江', '江苏', '上海', '黑龙江', '吉林', '辽宁', '内蒙古'
            , '山西', '河北', '天津', '北京']
        self.fenlei = ['按行业分城镇单位就业人员', '按行业分私营企业和个体就业人员', '按行业分城镇私营企业和个体就业人员',
                       '私营企业就业人员', '个体就业人员', '城镇单位就业人员工资总额和指数', '城镇单位就业人员平均工资和指数',
                       '按登记注册类型分城镇单位就业人员平均工资', '按行业分城镇单位就业人员工资总额',
                       '按行业分城镇单位就业人员平均工资', '按行业分城镇私营单位就业人员平均工资', '城镇登记失业人员及失业率']
        self.fenlei_min = ["农林牧渔业城镇单位就业人员", "采矿业城镇单位就业人员", "制造业城镇单位就业人员", "电力、热力、燃气及水生产和供应业城镇单位就业人员"
            , "建筑业城镇单位就业人员", "交通运输、仓储和邮政业城镇单位就业人员", "信息传输、软件和信息技术服务业城镇单位就业人员", "批发和零售业城镇单位就业人员"
            , "住宿和餐饮业城镇单位就业人员", "金融业城镇单位就业人员", "房地产业城镇单位就业人员", "租赁和商务服务业城镇单位就业人员", "科学研究和技术服务业城镇单位就业人员"
            , "水利、环境和公共设施管理业城镇单位就业人员", "居民服务、修理和其他服务业城镇单位就业人员", "教育业城镇单位就业人员", "卫生和社会工作城镇单位就业人员"
            , "文化、体育和娱乐业城镇单位就业人员", "公共管理、社会保障和社会组织城镇单位就业人员"]

    def get_data(self, fenlei):
        if fenlei is None:
            return None
        if fenlei == self.fenlei[0]:
            return self.work_hangye_chengzhen
        elif fenlei == self.fenlei[1]:
            return self.work_hangye_sige
        elif fenlei == self.fenlei[2]:
            return self.work_hangye_chengzhen_sige
        elif fenlei == self.fenlei[3]:
            return self.work_siying
        elif fenlei == self.fenlei[4]:
            return self.work_geti
        elif fenlei == self.fenlei[5]:
            return self.wage_chengzhen_zong
        elif fenlei == self.fenlei[6]:
            return self.wage_chengzhen_pingjun
        elif fenlei == self.fenlei[7]:
            return self.wage_zhuce_chengzhen_pingjun
        elif fenlei == self.fenlei[8]:
            return self.wage_hangye_chengzhen_zong
        elif fenlei == self.fenlei[9]:
            return self.wage_hangye_chengzhen_pingjun
        elif fenlei == self.fenlei[10]:
            return self.wage_hangye_chengzhensiying_pingjun
        elif fenlei == self.fenlei[11]:
            print("1")
            return self.shiye


@app.route('/bar_over_line')
def bar_over_line():
    bar_line_data = GetData()
    line_data0 = bar_line_data.df.query('industry == "信息传输、软件和信息技术服务业城镇单位就业人员" and city == "甘肃"')
    line_data1 = bar_line_data.df.query('industry == "信息传输、软件和信息技术服务业城镇单位就业人员平均工资" and city == "甘肃"')
    line_data2 = bar_line_data.df.query('industry == "信息传输、软件和信息技术服务业城镇私营单位就业人员平均工资" and city == "甘肃"')
    y_data0 = []
    y_data1 = []
    y_data2 = []
    x_data = []
    # display(line_data1)
    for i in range(3, 12):
        y_data0.append(str(line_data0.iloc[0, i]))
        y_data1.append(str(line_data1.iloc[0, i]))
        y_data2.append(str(line_data2.iloc[0, i]))
        x_data.append(str(2009 + i))
    print(y_data0)
    line = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="就业人员",
            y_axis=y_data0,
            yaxis_index=1
        )
    )
    bar_line = (
        Bar()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis("城镇就业工资", y_data1)
        .add_yaxis("城镇私营工资", y_data2)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} 万人"), interval=0.5
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="甘肃省计算机类工作"),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 元")),
        )
    )
    bar_line.overlap(line)
    # bar_line.render_notebook()
    return bar_line.dump_options_with_quotes()

@app.route('/bar', methods=['POST', 'GET'])
def bar():
    mydata = GetData()
    DF = mydata.get_data('按行业分城镇单位就业人员')
    fenleis = mydata.fenlei
    citys = mydata.city
    data_list = DF.query('city == "甘肃"')
    data_list = data_list.iterrows()

    return render_template("/test/test_ajax.html",datalist=data_list, citys=citys, fenleis=fenleis)

@app.route('/')
def index():
    # return render_template("/test/test_ajax.html")
    return render_template("/test/test_ajax_index.html")

if __name__ == '__main__':
    app.run(debug=True)

