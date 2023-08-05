import seaborn as sns


def multi_plot(col, ax, df, iti_palette, plotfunc, hue=None, top_n=10):
    order = df[col].value_counts().index[:top_n]
    clean_col_name = col.replace("_", " ").title()

    if hue:
        pkwarg = {"palette": iti_palette}
        ax.set_title("{} by {} - {:.0f} Missing".format(clean_col_name, hue,
                                                        df[col].isnull().sum()))
    else:
        pkwarg = {"color": next(iti_palette)}
        ax.set_title("{} - {:.0f} Missing".format(clean_col_name,
                                                  df[col].isnull().sum()))

    if plotfunc == sns.countplot:
        pkwarg['alpha'] = 0.5
        pkwarg['edgecolor'] = "black"
        pkwarg['linewidth'] = 1
        pkwarg['order'] = order
        if hue:
            pkwarg['hue'] = hue

    if plotfunc == sns.boxplot:
        if hue:
            pkwarg["x"] = hue

    plotfunc(data=df, y=col, ax=ax, **pkwarg)
    ax.set_ylabel(clean_col_name)
    ax.set_xlabel("Count")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def custom_distplot(col, ax, df, iti_palette, hue=None, top_n=10):
    valmin, valmax = df[col].min(), df[col].max()
    clean_col_name = col.replace("_", " ").title()

    if hue:
        hue_cats = df[hue].value_counts().index[:top_n]
        clean_huecol_name = hue.replace("_", " ").title()
        for h in hue_cats:
            pdf = df.loc[df[hue] == h, col]
            pal = next(iti_palette)
            sns.distplot(pdf, ax=ax, color=pal, kde_kws={"color": pal, "lw": 2}, label=h)
        ax.set_title("{} by {} - {:.0f} Missing".format(clean_col_name, clean_huecol_name,
                                                        df[col].isnull().sum()))
        ax.legend()
    else:
        sns.distplot(df[col], ax=ax, color=next(iti_palette), kde_kws={"color": "k", "lw": 2})
        ax.set_title("{}".format(clean_col_name))

    ax.set_xlim(valmin, valmax)
    ax.set_xlabel(clean_col_name)
    ax.set_ylabel("Density")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, lw=1, ls='--', c='.75')


def clean_str_arr(series):
    if series.shape[0] == 0:
        return "EMPTY"
    else:
        series = series.dropna().astype(str).str.lower().str.replace("none", "").str.title()
        return " ".join(series)


def plot_cloud(col, ax, df, title="WordCloud", cmap="plasma"):
    string = clean_str_arr(df[col].copy())
    wordcloud = WordCloud(width=800, height=500,
                          collocations=True,
                          background_color="black",
                          max_words=100,
                          colormap=cmap).generate(string)

    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_title(title, fontsize=18)
    ax.axis('off')


def single_bar(col, ax, df, x_var, iti_palette):
    sns.barplot(data=df,
                x=x_var,
                y=col,
                ax=ax,
                color=next(iti_palette),
                linewidth=1,
                alpha=.8)
    ax.set_title("{} by {}".format(col, x_var))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
