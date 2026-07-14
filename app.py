import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Min-Max using Divide & Conquer", page_icon="📊")

st.title("📊 Min-Max using Divide and Conquer")
st.write("Analysis of Divide and Conquer vs Naive Approach")

# Global comparison counter
comparison_count = 0


# Divide and Conquer Function
def min_max_dc(arr, low, high):
    global comparison_count

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]

    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


# Naive Method
def min_max_naive(arr):
    mn = arr[0]
    mx = arr[0]
    comps = 0

    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x

        comps += 1
        if x > mx:
            mx = x

    return mn, mx, comps


# ------------------ User Input ------------------

st.header("Enter Array")

choice = st.radio(
    "Choose Input Method",
    ("Manual Input", "Random Array")
)

if choice == "Manual Input":

    numbers = st.text_input(
        "Enter integers separated by commas",
        "3,1,7,4,9,2,8,5,6,0"
    )

    try:
        arr = [int(x.strip()) for x in numbers.split(",")]

    except:
        st.error("Please enter valid integers.")
        st.stop()

else:

    size = st.slider("Array Size", 5, 100, 10)

    arr = [random.randint(1, 100) for _ in range(size)]

    st.write("Generated Array")
    st.write(arr)


# ------------------ Run Algorithm ------------------

if st.button("Find Min & Max"):

    comparison_count = 0

    mn, mx = min_max_dc(arr, 0, len(arr)-1)

    dc_comp = comparison_count

    _, _, naive_comp = min_max_naive(arr)

    st.success("Result")

    col1, col2 = st.columns(2)

    col1.metric("Minimum", mn)
    col2.metric("Maximum", mx)

    st.write("### Comparison Count")

    st.write(f"**Divide & Conquer :** {dc_comp}")

    st.write(f"**Naive Method :** {naive_comp}")


# ------------------ Performance Analysis ------------------

st.header("Performance Analysis")

if st.button("Generate Performance Table"):

    sizes = [10, 100, 1000, 10000]

    data = []

    for size in sizes:

        arr = [random.randint(1, 10000) for _ in range(size)]

        comparison_count = 0

        mn, mx = min_max_dc(arr, 0, len(arr)-1)

        dc = comparison_count

        _, _, naive = min_max_naive(arr)

        formula = (3 * size) // 2 - 2

        data.append([size, dc, naive, formula])

    df = pd.DataFrame(
        data,
        columns=[
            "Array Size",
            "D&C Comparisons",
            "Naive Comparisons",
            "3n/2 - 2"
        ]
    )

    st.dataframe(df, use_container_width=True)

    st.line_chart(
        df.set_index("Array Size")[["D&C Comparisons", "Naive Comparisons"]]
    )

st.markdown("---")
st.caption("Design and Analysis of Algorithms Lab")
